# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
import pref

x = pref.x
y = pref.y+18


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    wool0 = "wool:" + placeholders[0]
    wool1 = "wool:" + placeholders[1]
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    z = int(mc.send_cmd("get_player_z " + mtuser))
    # Check that builder_police happy that task completed
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
        task = int(mc.send_cmd("get_player_task " + mtuser))
        if task > 6:
            passed()
        else:
            failed("Failed: Check 'Task 6 Assessment' sign in minetest to find out what else is required")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
