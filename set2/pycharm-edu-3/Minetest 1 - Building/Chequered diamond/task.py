from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

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
mc.build(range(x1, x2), range(y1, y2), z, "air")

# build diamond
for y in range(y1, y2):
    # calculate x range which will give diamond shape
    xlo = x1 + abs(y - cy)
    xhi = x2 - abs(y - cy)
    for x in range(xlo, xhi):
        # set each node to an alternate wool colour using same formula as in previous task
        mc.build(x, y, z, colours[(x + y) % 2])
mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo sessions in 2018 - 2019.
