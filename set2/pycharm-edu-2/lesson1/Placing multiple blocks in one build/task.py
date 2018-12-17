from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

ref_x = 100
ref_y = 14
ref_z = player_z
wool = "wool:yellow"
glass = "default:glass"

seq_x = (ref_x - 1, ref_x, ref_x + 1)
seq_y = (ref_y - 1, ref_y, ref_y + 1)
seq_z = (ref_z - 1, ref_z, ref_z + 1)
mc.build(seq_x, seq_y, seq_z, glass)
mc.build(ref_x, ref_y, ref_z, wool)
mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2019.
