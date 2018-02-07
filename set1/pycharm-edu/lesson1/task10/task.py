from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# start point of tunnel
x1 = 69
y1 = 14
z = int(mc.send_cmd('get_player_z ' + mtuser))

# store node types in variables for easier use
stair = '{"name":"stairs:stair_stonebrick","param2":"1"}'
rail  = 'carts:rail'
prail = 'carts:powerrail'
node_lists = {stair:[], rail:[], prail:[]}

for i in range(61):
    #Add stairs - Don't need stairs on very last block. Hence check i < 60
    if i < 60:
        #mc.set_node(x1-i,y1-i,z-1,stair)
        node_lists[stair].append((x1-i,y1-i,z-1))
    #Add power rail
    #mc.set_node(x1-i,y1-i+1,z,prail)
    node_lists[prail].append((x1-i,y1-i+1,z))
for x in range(x1,93+1):
    #Add rail or powerrail in pairs
    if x//2%2==0:
        #mc.set_node(x,y1+1,z,rail)
        node_lists[rail].append((x,y1+1,z))
    else:
        #mc.set_node(x,y1+1,z,prail)
        node_lists[prail].append((x,y1+1,z))
for item in node_lists:
    mc.set_node_list(node_lists[item], item)




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
