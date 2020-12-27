from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

mc.build(100, 14, number, "wool:green")
mc.send_building()


# © Copyright 2018-2021 Triptera Pty Ltd
# https://www.pythonator.com
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2021.
