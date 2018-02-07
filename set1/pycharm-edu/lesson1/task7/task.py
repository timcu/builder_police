from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# position of centre of diamond
cx = 100
cy = 32
z = int(mc.send_cmd('get_player_z ' + mtuser))

# array of node types which we will alternate through
colours = ["wool:white", "wool:orange"]
# initialise an empty list of positions for each of the colours
node_lists = { colour: [] for colour in colours }

# calculate extents of diamond
width = 21
height = 21
x1 = cx - width // 2
y1 = cy - height // 2
x2 = x1 + width
y2 = y1 + height

for y in range(y1,y2):
    # calculate x range which will give diamond shape
    xlo = x1 + abs(y - cy)
    xhi = x2 - abs(y - cy)
    for x in range(xlo,xhi):
        # set each node to an alternate wool colour by adding position to node list
        node_lists[colours[(x+y)%2]].append((x, y, z))
# set all nodes of each colour
for colour in colours:
    mc.set_node_list(node_lists[colour], colour)




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
