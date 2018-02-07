from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# position of centre of square
cx = 100
cy = 32
z = int(mc.send_cmd('get_player_z ' + mtuser))

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
node_lists = {colour0: [], colour1: []}
for y in range(y1, y2):
    for x in range(x1, x2):
        colour = colours[(y+x)%2]
        node_lists[colour].append((x, y, z))
for colour in colours:
    mc.set_node_list(node_lists[colour], colour)




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
