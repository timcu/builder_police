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
    pz = int(str_z_correct)
    for y in range(pref.y-1, pref.y+2):
        for z in range(pz-1, pz+2):
            node=mc.get_node(pref.x,y,z)
            if y == pref.y and z == pz:
                if node[0:5] != "wool:":
                    failed("center node type does not start with 'wool:'. It is '" + node + "'")
                    return False
            else:
                if node != "default:glass":
                    failed("Node at x="+str(pref.x)+", y="+str(y)+", z="+str(z)+" should be 'default:glass' but is '" + node + "'" )
                    return False
    passed()
    return True


def test_formula(placeholders, i, answer, list_data):
    phi = placeholders[i]
    stri = str(i+1)
    if len(phi) > len(answer) + 5:
        failed("Answer " + stri + " is too long. Correct answer only " + str(len(answer)) + " characters long. Your answer " + phi + " has length " + str(len(phi)))
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
            failed("Answer " + stri + " should only be in terms of variables " + list_vars + " but includes other variables. It is " + phi )
        correct = eval(phi, data)
        if guess != correct:
            failed("Answer " + str + " gave incorrect answer for data " + str(data) + ". Correct answer: " + correct + ". Your answer: " + guess + ". Your formula: " + phi)
            return False
    return True


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_formula(placeholders, 1, 'y-1', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 2, 'z+1', [{'z':20}, {'z':50}] ): return False
    if not test_formula(placeholders, 3, 'y+1', [{'y':14}, {'y':16}] ): return False
    if not test_formula(placeholders, 4, 'x', [{'x':100}, {'x':50}] ): return False
    if not test_formula(placeholders, 5, 'y', [{'y':14}, {'y':16}] ): return False
    passed()
    return True


if __name__ == '__main__':
    #run_common_tests()
    if test_answer_placeholders():
        test_nodes()


