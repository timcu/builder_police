from ircbuilder import open_irc
from ircbuilder.building import Building

from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

ref_x = 101
ref_y = 14
ref_z = player_z
glass = "default:obsidian_glass"

for y in (ref_y - 1, ref_y, ref_y + 1):
    for z in (ref_z - 1, ref_z, ref_z + 1):
        b.build(ref_x, y, z, glass)
        print("y", y, "z", z)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
