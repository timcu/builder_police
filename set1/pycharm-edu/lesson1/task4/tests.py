# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
import pref

x1 = pref.x-7
x2 = pref.x-30
y = pref.y


def test_nodes():
    placeholders = get_answer_placeholders()
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    str_z = placeholders[3]
    str_z_correct = mc.send_cmd("get_player_z " + mtuser)
    if str_z_correct != str_z:
        failed("You are using incorrect z value=" + str_z + ". Should be " + str_z_correct)
        return False
    z = int(str_z)
    # roof
    str_count = mc.compare_nodes(x1, y+6, z-2, x2, y+6, z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel roof at y=" + str(y+6) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # left wall
    str_count = mc.compare_nodes(x1, y  , z-2, x2, y+6, z-2, "default:glass")
    if str_count != '0':
        failed("Tunnel wall at z=" + str(z-2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # right wall
    str_count = mc.compare_nodes(x1, y  , z+2, x2, y+6, z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel wall at z=" + str(z+2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # floor
    str_count = mc.compare_nodes(x1, y  , z-2, x2, y  , z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel floor at z=" + str(z+2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # Air
    str_count = mc.compare_nodes(x1, y+1, z-1, x2, y+5, z+1, "air")
    if str_count != '0':
        failed("Tunnel centre should be all air but there are " + str_count + " blocks which are not")
        return False
    passed()
    return True


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()

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
    if not test_string(placeholders, 0, str(x1)): return False
    if not test_string(placeholders, 1, str(x2)): return False
    if not test_string(placeholders, 2, str(y)): return False
    if not test_formula(placeholders, 4, 'y'  , [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 5, 'z-2', [{'z':20}, {'z':50}] ): return False
    if not test_formula(placeholders, 6, 'y+6', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 7, 'z+2', [{'z':20}, {'z':50}] ): return False
    if not test_formula(placeholders, 8, 'y+1', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 9, 'z-1', [{'z':20}, {'z':50}] ): return False
    if not test_formula(placeholders,10, 'y+5', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders,11, 'z+1', [{'z':20}, {'z':50}] ): return False
    passed()
    return True


if __name__ == '__main__':
    #run_common_tests()
    if test_answer_placeholders():
        test_nodes()


