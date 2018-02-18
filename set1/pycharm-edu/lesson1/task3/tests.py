# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
from triptera_pe_tests import test_eval, test_eval_phi, test_string
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


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_eval(placeholders, 1, 'x+1', [{'x':50}, {'x':100}] ): return False
    if not test_eval(placeholders, 2, 'y+1', [{'y':14}, {'y':16}] ): return False
    if not test_eval(placeholders, 3, 'z+1', [{'z':20}, {'z':50}] ): return False
    if not test_string (placeholders, 4, 'glass'): return False
    if not test_eval(placeholders, 5, "x, y, z", [{'x':100, 'y':14, 'z':0}]): return False
    if placeholders[6].find("wool:") != 0:
        failed("Answer 7 should start with 'wool:'. Your answer is '" + placeholders[6] + "'")
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()
        test_nodes()
