from ircbuilder import open_irc
from ircbuilder.building import Building

from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z
from triptera_pe_tests import configure_logging

b = Building()

ref_x = 100
ref_y = 14
ref_z = player_z  # Alternatively type your unique z value instead of player_z
wool = "wool:blue"

b.build(ref_x, ref_y, ref_z, wool)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
