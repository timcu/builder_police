from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# end points of sloping section of tunnel (centre of floor)
x1 = 69
y1 = 14
x2 = 9
y2 = -46
z = int(mc.send_cmd('get_player_z ' + mtuser))


#Make the full tunnel in solid glass and stone first
for i in range(61):
    # Cross section of tunnel at position i
    # Build 5 x 7 blocks of glass at position i for walls, roof, and centre
    mc.set_nodes(x1-i,y1-i,z-2,x1-i,y1-i+6,z+2,"default:glass")
    # Build 3 x 1 blocks of stone at position i for floor
    mc.set_nodes(x1-i,y1-i,z-1,x1-i,y1-i  ,z+1,"default:stone")
# hollow out the tunnel because now we are sure that lava and water can't flow in the ends
for i in range(61):
    # Use air to hollow out the tunnel
    mc.set_nodes(x1-i,y1-i+1,z-1,x1-i,y1-i+5,z+1,"air")
    if i%4==0:
        # Place torches down the right hand side of the tunnel
        mc.set_node(x1-i,y1-i+1,z+1,"default:torch")




# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
