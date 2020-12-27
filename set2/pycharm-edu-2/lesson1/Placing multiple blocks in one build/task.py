from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

ref_x = 100
ref_y = 14
ref_z = player_z
wool = "wool:yellow"
glass = "default:glass"

seq_x = (ref_x - 1, ref_x, ref_x + 1)  # or (99, 100, 101)
seq_y = (ref_y - 1, ref_y, ref_y + 1)  # or (13, 14, 15)
seq_z = (ref_z - 1, ref_z, ref_z + 1)
mc.build(seq_x, seq_y, seq_z, glass)
mc.build(ref_x, ref_y, ref_z, wool)

mc.send_building()


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
