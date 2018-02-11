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
    str_z = placeholders[2]
    str_z_correct = mc.send_cmd("get_player_z " + mtuser)
    if str_z_correct != str_z:
        failed("You are using incorrect z value=" + str_z + ". Should be " + str_z_correct)
        return False
    str_node=mc.get_node(pref.x,pref.y,int(str_z))
    #print(str_node)
    if len(str_node) < 5 or str_node[0:5] != "wool:":
        failed("Centre node type does not start with 'wool:'. Is currently '" + str_node + "'")
        return False
    passed()
    return True


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    str_x = placeholders[0]
    str_y = placeholders[1]
    if str_x != str(pref.x):
        failed("You are using incorrect x value=" + str_x + ". Should be " + str(pref.x))
        print("This line is after failed")
        return False
    if str_y != str(pref.y):
        failed("You are using incorrect y value=" + str_y + ". Should be " + str(pref.y))
        print("This line is after failed")
        return False
    print("This line is before passed")
    passed()
    print("This line is after passed")
    return True

if __name__ == '__main__':
    # run_common_tests()
    if test_answer_placeholders():
        test_nodes()


