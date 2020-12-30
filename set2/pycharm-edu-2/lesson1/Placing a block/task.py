from ircbuilder import open_irc
from ircbuilder.building import Building
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel

b = Building()

b.build(100, 14, 20, "wool:green")

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
