from ircbuilder import open_irc
from ircbuilder.building import Building

from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel

b = Building()

b.build(100, 14, 0, "wool:green")

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
