# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel


def test_minetest():
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    task = int(mc.send_cmd("get_player_task " + mtuser))
    if task > 8:
        passed()
        return True
    else:
        failed("Failed: Check 'Task 8 Assessment' sign in minetest to find out what else is required")
        return False


def test_answer_placeholders():
    x1 = 69
    y1 = 14
    x2 = 9
    y2 = -46
    placeholders = get_answer_placeholders()
    ph = placeholders[0]
    if len(ph)>10:
        return failed("range for i should be calculated from formula which is less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    if "x" in ph:
        if "x1" not in ph or "x2" not in ph:
            return failed("range for i should be calculated from formula based on x1 and x2. Instead it is " + ph)
        try:
            r=eval(ph)
            if r!=61:
                return failed("range formula for i should evaluate to 61. Instead it evaluates to " + str(r))
        except NameError:
            return failed("range formula for i should only be based on x1 and x2. Instead it is " + ph)
    elif "y" in ph:
        if "y1" not in ph or "y2" not in ph:
            return failed("range for i should be calculated from formula based on y1 and y2")
        try:
            r=eval(ph)
            if r!=61:
                return failed("range formula for i should evaluate to 61. Instead it evaluates to " + str(r))
        except NameError:
            return failed("range formula for i should only be based on y1 and y2. Instead it is " + ph)
    else:
        return failed("range formula for i should be a formula based on x1 and x2 or y1 and y2. Instead it is " + ph)

    ph=placeholders[1]
    if len(ph)>10:
        return failed("x should be calculated from formula which is less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    if "x1" not in ph or "i" not in ph:
        failed("x should be calculated from formula based on x1 and i. Instead it is " + ph)
        return
    i=30
    try:
        r=eval(ph)
        if r!=x1-i:
            return failed("x value at i=30 should be " + str(x1-i) + ". Instead it is " + str(r))
    except NameError:
        return failed("x formula should only be based on x1 and i. Instead it is " + ph)

    ph=placeholders[2]
    if len(ph)>10:
        return failed("y should be calculated from formula which is less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    if "y1" not in ph or "i" not in ph:
        failed("y should be calculated from formula based on y1 and i. Instead it is " + ph)
        return
    i=10
    try:
        r=eval(ph)
        if r!=y1-i:
            return failed("y value at i=10 should be " + str(y1-i) + ". Instead it is " + str(r))
    except NameError:
        return failed("y formula should only be based on y1 and i. Instead it is " + ph)

    ph=placeholders[3]
    if len(ph)>10:
        return failed("torch condition should be less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    if "i" not in ph and "x" not in ph and "y" not in ph:
        failed("torch condition should be based on i (or x or y). Instead it is " + ph)
        return
    count=0
    try:
        for i in range(x1-x2+1):
            x = x1-i
            y = y1-i
            if eval(ph):
                count += 1
        if count >= 61 / 3 or count <= 61 / 5:
            return failed("torch condition returned True " + str(count) + " times but it should be between 12 and 20 times")
    except NameError:
        return failed("torch condition should only be based on i or x or y. Instead it is " + ph)
    passed()


if __name__ == '__main__':
    test_answer_placeholders()
    run_common_tests()
    test_minetest()

