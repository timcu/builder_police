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
    print("about to connect as ",pybotnick, mtuser)
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    str_z = placeholders[0]
    str_z_correct = mc.send_cmd("get_player_z " + mtuser)
    if str_z_correct != str_z:
        failed("You are using incorrect z value=" + str_z + ". Should be " + str_z_correct)
        return False
    z = int(str_z)
    # floor
    str_count = mc.compare_nodes(x1, y  , z-1, x2, y  , z+1, "default:stone")
    if str_count != '0':
        failed("Tunnel floor at z=" + str(z+2) + " should be all stone but there are " + str_count + " blocks which are not")
        return False
    # torches
    str_count = mc.compare_nodes(x1, y+1, z-1, x2, y+1, z+1, "air")
    count_not_air = int(str_count)
    str_count = mc.compare_nodes(x1, y+1, z-1, x2, y+1, z+1, "default:torch")
    count_not_torch = int(str_count)
    count_other = (x1-x2+1)*3 - count_not_torch - count_not_air
    if count_other > 0:
        failed("Above floor should only be air or torches but " + str(count_other) + " nodes are something else")
        return False
    min_torch = (x1-x2)//4
    if count_not_air < min_torch:
        failed("There should be at least " + str(min_torch) + " torches but there are only " + str(count_not_air))
        return False
    if count_not_air > min_torch+1:
        failed("There should be at most " + str(min_torch+1) + " torches but there are " + str(count_not_air))
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
    #run_common_tests()
    #if test_answer_placeholders():
    test_nodes()


