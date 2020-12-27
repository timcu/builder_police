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


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
