from ircbuilder import open_irc
from ircbuilder.building import Building

from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# position of centre of diamond
cx = 100
cy = 32
z = player_z

# array of node types which we will alternate through
colours = ["wool:white", "wool:orange"]

# calculate extents of diamond
width = 21
height = 21
x1 = cx - width // 2
y1 = cy - height // 2
x2 = x1 + width
y2 = y1 + height

# clear area first with air
b.build(range(x1, x2), range(y1, y2), z, "air")

# build diamond
for y in range(y1, y2):
    # calculate x range which will give diamond shape
    xlo = x1 + abs(y - cy)
    xhi = x2 - abs(y - cy)
    for x in range(xlo, xhi):
        # set each node to an alternate wool colour using same formula as in previous task
        b.build(x, y, z, colours[(x + y) % 2])

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
