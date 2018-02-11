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


def test_formula_phi(phi, stri, answer, list_data):
    if len(phi) > len(answer) + 5:
        failed(stri + " is too long. Correct answer only " + str(len(answer)) + " characters long. Your answer " + phi + " has length " + str(len(phi)))
        return False
    for data in list_data:
        try:
            guess = eval(phi, data)
        except NameError:
            list_vars = ""
            comma = ""
            for k in data:
                list_vars += comma + k
                comma = ", "
            failed(stri + " should only be in terms of variables " + list_vars + " but includes other variables. It is " + phi )
        correct = eval(phi, data)
        if guess != correct:
            failed(str + " gave incorrect answer for data " + str(data) + ". Correct answer: " + correct + ". Your answer: " + guess + ". Your formula: " + phi)
            return False
    return True


def test_formula(placeholders, i, answer, list_data):
    stri = "Answer " + str(i+1)
    return test_formula_phi(placeholders[i], stri, answer, list_data)


def test_string(placeholders, i, answer):
    phi = placeholders[i]
    stri = "Answer " + str(i+1)
    if phi != answer:
        failed(stri + " should be " + answer + ". You entered " + phi)
        return False
    return True


def test_string_in(placeholders, i, list_answer):
    phi = placeholders[i]
    stri = "Answer " + str(i+1)
    if phi not in list_answer:
        failed(stri + " should be one of " + str(list_answer) + ". You entered " + phi)
        return False
    return True


def test_answer_placeholders():
    x1 = 69
    y1 = 14
    x2 = 9
    y2 = -46
    placeholders = get_answer_placeholders()
    if not test_formula(placeholders, 0, 'x1-x2+1', [{'x1':69, 'x2':9}, {'x1':70, 'x2':35}]): return False
    if not test_formula(placeholders, 1, 'x1-i', [{'x1':69, 'i':0}, {'x1': 70, 'i':35}]): return False
    if not test_formula(placeholders, 2, 'y1-i', [{'y1':14, 'i':0}, {'y1':-46, 'i':15}]): return False

    ph=placeholders[3]
    if len(ph)>10:
        return failed("torch condition should be less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    count=0
    try:
        for i in range(x1-x2+1):
            x = x1-i
            y = y1-i
            if eval(ph, {'i':i, 'x':x, 'y':y}):
                count += 1
        if count >= 61 / 3 or count <= 61 / 5:
            failed("torch condition returned True " + str(count) + " times but it should be between 12 and 20 times")
            return False
    except NameError:
        failed("torch condition should only be based on i or x or y. Instead it is " + ph)
        return False
    passed()


if __name__ == '__main__':
    test_answer_placeholders()
    #run_common_tests()
    test_minetest()

