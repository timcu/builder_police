from ircbuilder import open_irc
from ircbuilder.building import Building

from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# player_z has been imported from the configuration file you created in first task
ref_z = player_z
glass = "default:obsidian_glass"

for y in (13, 14, 15):
    b.build(99, y, ref_z - 1, glass)
    b.build(99, y, ref_z, glass)
    b.build(99, y, ref_z + 1, glass)
    print(y)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
