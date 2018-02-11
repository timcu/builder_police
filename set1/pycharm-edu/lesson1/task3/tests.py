# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
import pref


def test_nodes():
    placeholders = get_answer_placeholders()
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    print("about to connect as ",pybotnick, mtuser)
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    str_z = placeholders[0]
    str_z_correct = mc.send_cmd("get_player_z " + mtuser)
    if str_z_correct != str_z:
        failed("You are using incorrect z value=" + str_z + ". Should be " + str_z_correct)
        return False
    z = int(str_z_correct)
    str_count = mc.compare_nodes(pref.x-1, pref.y-1, z-1, pref.x+1, pref.y+1, z+1, "default:glass")
    if str_count != '1':
        failed("Cube should contain 1 block which is not glass. Yours contained " + str_count)
        return False
    passed()
    return True


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


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_formula(placeholders, 1, 'x+1', [{'x':50}, {'x':100}] ): return False
    if not test_formula(placeholders, 2, 'y+1', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 3, 'z+1', [{'z':20}, {'z':50}] ): return False
    if not test_string (placeholders, 4, 'glass'): return False
    list_var = [x.strip() for x in placeholders[5].strip().split(",")]
    if len(list_var) != 3:
        failed("Wrong number of arguments in answer 6. Should be 3. You have " + str(len(list_var)))
        return False
    if not test_formula_phi(list_var[0], "First argument in answer 6" , 'x', [{'x':100}, {'x':50}] ): return False
    if not test_formula_phi(list_var[1], "Second argument in answer 6", 'y', [{'y':100}, {'y':50}] ): return False
    if not test_formula_phi(list_var[2], "Third argument in answer 6" , 'z', [{'z':100}, {'z':50}] ): return False
    if placeholders[6].find("wool:") != 0:
        failed("Answer 7 should start with 'wool:'. Your answer is '" + placeholders[6] + "'")
        return False
    passed()
    return True


if __name__ == '__main__':
    #run_common_tests()
    if test_answer_placeholders():
        test_nodes()
