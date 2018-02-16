# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import failed, passed
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel


def test_minetest(num_task):
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    task = int(mc.send_cmd("get_player_task " + mtuser))
    if task > num_task:
        passed()
        return True
    else:
        failed("Failed: Check 'Task " + str(num_task) + " Assessment' sign in minetest to find out what else is required")
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


