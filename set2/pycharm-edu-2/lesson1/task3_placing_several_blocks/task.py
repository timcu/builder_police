from ircbuilder import open_irc
from ircbuilder.building import Building

from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

ref_z = player_z
wool = "wool:red"
glass = "default:glass"

b.build(100, 13, ref_z - 1, glass)
b.build(100, 14, ref_z - 1, glass)
b.build(100, 15, ref_z - 1, glass)
b.build(100, 13, ref_z, glass)
b.build(100, 14, ref_z, wool)
b.build(100, 15, ref_z, glass)
b.build(100, 13, ref_z + 1, glass)
b.build(100, 14, ref_z + 1, glass)
b.build(100, 15, ref_z + 1, glass)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
