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
    for x in range(pref.x-1, pref.x+2):
        for y in range(pref.y-1, pref.y+2):
            for z in range(pref.z-1, pref.z+2):
                node=mc.get_node(x,y,z)
                if y == pref.y and z == pref.z:
                    if node[0:5] != "wool:":
                        failed("center node type does not start with 'wool:'. It is '" + node + "'")
                        return False
                else:
                    if node != "default:glass":
                        failed("Node at x="+str(x)+", y="+str(y)+", z="+str(z)+" should be 'default:glass' but is '" + node + "'" )
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


if __name__ == '__main__':
    run_common_tests()
    #test_answer_placeholders():
    test_nodes()
