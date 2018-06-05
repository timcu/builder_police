from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

ref_x = 101
ref_y = 14
ref_z = player_z
glass = "default:obsidian_glass"

for y in (ref_y - 1, ref_y, ref_y + 1):
    for z in (ref_z - 1, ref_z, ref_z + 1):
        mc.build(ref_x, y, z, glass)
        print("y", y, "z", z)
mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018.
