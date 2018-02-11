# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
import pref

x = pref.x
y = pref.y+18


def test_nodes():
    placeholders = get_answer_placeholders()
    wool0 = "wool:" + placeholders[0]
    wool1 = "wool:" + placeholders[1]
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    z = int(mc.send_cmd("get_player_z " + mtuser))
    # floor
    count_0 = 81 - int(mc.compare_nodes(x-4, y-4, z, x+4, y+4, z, wool0))
    count_1 = 81 - int(mc.compare_nodes(x-4, y-4, z, x+4, y+4, z, wool1))
    if count_0 > 45:
        failed("Too many " + wool0 + ". Should be less than 46 but are " + count_0)
    elif count_1 > 45:
        failed("Too many " + wool1 + ". Should be less than 46 but are " + count_1)
    elif count_0 < 36:
        failed("Too few " + wool0 + ". Should be at least 36 but are " + count_0)
    elif count_1 < 36:
        failed("Too few " + wool1 + ". Should be at least 36 but are " + count_1)
    else:
        # Check that builder_police happy that task completed
        task = int(mc.send_cmd("get_player_task " + mtuser))
        if task > 6:
            passed()
        else:
            failed("Failed: Check 'Task 6 Assessment' sign in minetest to find out what else is required")


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
    placeholders = get_answer_placeholders()
    list_wool = ["white", "grey", "dark_grey", "black", "blue", "cyan", "green", "dark_green", "yellow", "orange", "brown", "red", "pink", "magenta", "violet"]
    if not test_string_in(placeholders, 0, list_wool): return False
    if not test_string_in(placeholders, 1, list_wool): return False
    if not test_string(placeholders, 2, '9'): return False
    if not test_string(placeholders, 3, '9'): return False
    if not test_formula(placeholders, 4, 'cx - width // 2', [{'cx':100, 'width':9}, {'cx':110, 'width':21}] ): return False
    if not test_formula(placeholders, 5, 'cy - height // 2', [{'cy':14, 'height':9}, {'cy':15, 'height':21}] ): return False
    list_var = [x.strip() for x in placeholders[6].strip().split(",")]
    if len(list_var) != 2 and len(list_var) != 3:
        failed("Wrong number of arguments in answer 7. Should be 2 (or 3). You have " + str(len(list_var))) + str(list_var)
        return False
    if not test_formula_phi(list_var[0], "First argument in answer 7" , 'y1', [{'y1':28}, {'y1':36}] ): return False
    if not test_formula_phi(list_var[1], "Second argument in answer 7", 'y2', [{'y2':28}, {'y2':36}] ): return False
    list_var = [x.strip() for x in placeholders[7].strip().split(",")]
    if len(list_var) != 2 and len(list_var) != 3:
        failed("Wrong number of arguments in answer 8. Should be 2 (or 3). You have " + str(len(list_var)))
        return False
    if not test_formula_phi(list_var[0], "First argument in answer 8" , 'x1', [{'x1':96}, {'x1':104}] ): return False
    if not test_formula_phi(list_var[1], "Second argument in answer 8", 'x2', [{'x2':96}, {'x2':104}] ): return False
    # Can't test 8 because may have formula over several lines
    #if not test_formula(placeholders, 6, 'colours[(y+x)%2]')
    passed()
    return True


if __name__ == '__main__':
    #run_common_tests()
    if test_answer_placeholders():
        test_nodes()
