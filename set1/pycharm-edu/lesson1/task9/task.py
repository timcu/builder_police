from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
from math import floor

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# end points of sloping section of tunnel (centre of floor)
x1 = 69
y1 = 14
x2 = 9
y2 = -46
z = int(mc.send_cmd('get_player_z ' + mtuser))

# node types
glass = "default:glass"
stone = "default:stone"
air   = "air"
torch = "default:torch"
node_lists = {glass: [], stone: [], air: [], torch: []}
node_dict = {}

def set_node(x, y, z, item):
    "similar to mc.set_node but stores nodes in nodes_map rather than sending to minetest"
    # convert x, y, z to integers so that each node has unique set of coordinates
    node_dict[(floor(x + 0.5), floor(y + 0.5), floor(z + 0.5))]=item

def set_nodes(x1, y1, z1, x2, y2, z2, item):
    "similar to mc.set_nodes but stores nodes in nodes_map rather than sending to minetest"
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    zstep = 1 if z2 > z1 else -1
    for z in range(z1, z2 + zstep, zstep):
        for y in range(y1, y2 + ystep, ystep):
            for x in range(x1, x2 + xstep, xstep):
                set_node(x, y, z, item)

for i in range(x1-x2+1):
    # coordinates at position i in tunnel
    x = x1 - i
    y = y1 - i
    # Build 5 x 7 blocks of glass at position i for walls, roof, and centre
    set_nodes(x,y,z-2,x,y+6,z+2,glass)
    # Build 3 x 1 blocks of stone at position i for floor
    set_nodes(x,y,z-1,x,y  ,z+1,stone)
    # Now hollow out the tunnel because sure that lava and water can't seep in
    # Use air to hollow out the tunnel
    set_nodes(x,y+1,z-1,x,y+5,z+1,air)
    if i%4==0:
        # Place torches down the right hand side of the tunnel
        set_node(x,y+1,z+1,torch)

# Convert node_dict to node_lists
for pos, item in node_dict.items():
    node_lists[item].append(pos)
# Send node_lists to minetest. Should send air after walls so no lava and water flow in
for item in (glass, stone, air, torch):
    node_list = node_lists[item]
    mc.set_node_list(node_list, item)




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
