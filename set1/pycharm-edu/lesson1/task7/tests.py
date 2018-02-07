# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018



from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel


def test_minetest():
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    task = int(mc.send_cmd("get_player_task " + mtuser))
    if task > 7:
        passed()
        return True
    else:
        failed("Failed: Check 'Task 7 Assessment' sign in minetest to find out what else is required")
        return False

if __name__ == '__main__':
    if not test_minetest():
        run_common_tests()
        #test_answer_placeholders()


