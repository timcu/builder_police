from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

ref_z = player_z
wool = "wool:red"
glass = "default:glass"

mc.build(100, 13, ref_z - 1, glass)
mc.build(100, 14, ref_z - 1, glass)
mc.build(100, 15, ref_z - 1, glass)
mc.build(100, 13, ref_z, glass)
mc.build(100, 14, ref_z, wool)
mc.build(100, 15, ref_z, glass)
mc.build(100, 13, ref_z + 1, glass)
mc.build(100, 14, ref_z + 1, glass)
mc.build(100, 15, ref_z + 1, glass)

mc.send_building()


# © Copyright 2018-2021 Triptera Pty Ltd
# https://pythonator.com
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2021.
