from ircbuilder import open_irc
from ircbuilder.building import Building

from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

ref_x = 100
ref_y = 14
ref_z = player_z  # Alternatively type your unique z value instead of player_z
wool = "wool:blue"

b.build(ref_x, ref_y, ref_z, wool)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
