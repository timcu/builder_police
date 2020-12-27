from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

mc.build(100, 14, 0, "wool:green")

mc.send_building()


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
