from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# player_z has been imported from the configuration file you created in first task
ref_z = player_z
glass = "default:obsidian_glass"

for y in (13, 14, 15):
    mc.build(99, y, ref_z - 1, glass)
    mc.build(99, y, ref_z, glass)
    mc.build(99, y, ref_z + 1, glass)
    print(y)
mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018.
