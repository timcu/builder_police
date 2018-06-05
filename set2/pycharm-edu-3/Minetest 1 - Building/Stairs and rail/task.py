from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# start point of tunnel
x1 = 69
x2 = 9
task4_x1 = 93
y1 = 14
z = player_z
num_segments = x1 - x2 + 1

# store node types in variables for easier use
stair_up_x = '{"name":"stairs:stair_stonebrick","param2":"1"}'
rail  = 'carts:rail'
power_rail = 'carts:powerrail'

# sloping section of tunnel
for i in range(num_segments):
    #Add stairs - Don't need stairs on very last block. Hence check i < 60
    if i < 60:
        mc.build(x1 - i, y1 - i, z - 1, stair_up_x)
    #Add power rail
    mc.build(x1 - i, y1 - i + 1, z, power_rail)

# flat section of tunnel
for x in range(x1,task4_x1+1):
    #Add rail or power rail in pairs
    if x//2%2==0:
        mc.build(x, y1 + 1, z, rail)
    else:
        mc.build(x, y1 + 1, z, power_rail)
mc.send_building()



# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
