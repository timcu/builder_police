from ircbuilder import open_irc
from ircbuilder.building import Building
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# position of centre of square
cx = 100
cy = 32
z = player_z

# array of node types which we will alternate through
colour0 = "wool:green"
colour1 = "wool:blue"
colours = [colour0, colour1]

# calculate extents of square
width = 9
height = 9
x1 = cx - width // 2
y1 = cy - height // 2
x2 = x1 + width
y2 = y1 + height

# loop through all positions in square
for y in range(y1, y2):
    for x in range(x1, x2):
        colour = colours[(y + x) % 2]
        b.build(x, y, z, colour)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
