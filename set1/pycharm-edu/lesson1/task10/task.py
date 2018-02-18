from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# start point of tunnel
x1 = 69
task4_x1 = 93
y1 = 14
z = int(mc.send_cmd('get_player_z ' + mtuser))

# store node types in variables for easier use
STAIR_UP_X = '{"name":"stairs:stair_stonebrick","param2":"1"}'
RAIL  = 'carts:rail'
POWER_RAIL = 'carts:powerrail'
node_lists = {STAIR_UP_X:[], RAIL:[], POWER_RAIL:[]}

for i in range(61):
    #Add stairs - Don't need stairs on very last block. Hence check i < 60
    if i < 60:
        node_lists[STAIR_UP_X].append((x1 - i, y1 - i, z - 1))
    #Add power rail
    node_lists[POWER_RAIL].append((x1 - i, y1 - i + 1, z))
for x in range(x1,task4_x1+1):
    #Add rail or power rail in pairs
    if x//2%2==0:
        node_lists[RAIL].append((x, y1 + 1, z))
    else:
        node_lists[POWER_RAIL].append((x, y1 + 1, z))
for item in node_lists:
    mc.set_node_list(node_lists[item], item)




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
