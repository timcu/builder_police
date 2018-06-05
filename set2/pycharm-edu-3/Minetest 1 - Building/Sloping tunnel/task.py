from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# Location of end points of sloping section of tunnel (centre of floor)
x1 = 69
y1 = 14
x2 = 9
y2 = -46
ref_z = player_z

# Dimensions
height_tunnel = 7
width_tunnel = 5
num_segments = x1 - x2 + 1

# Building materials
glass = "default:glass"
floor = "default:stone"
torch = "default:torch"
air = "air"

#Make the full tunnel in solid glass and stone first
for i in range(num_segments):
    # Cross section of tunnel at position i
    # x, y, z are coordinates of lower left corner of segment of tunnel
    x = x1 - i
    y = y1 - i
    z = ref_z - width_tunnel // 2
    # Build 5 x 7 blocks of glass at position i for walls, roof, and centre
    range_y_ext = range(y, y + height_tunnel)
    range_z_ext = range(z, z + width_tunnel)
    mc.build(x, range_y_ext, range_z_ext, glass)
    # Build 3 x 1 blocks of stone at position i for floor
    range_z_floor = (z + 1, z + 2, z + 3)
    mc.build(x, y, range_z_floor, floor)
# hollow out the tunnel because now we are sure that lava and water can't flow in the ends
for i in range(num_segments):
    # Use air to hollow out the tunnel
    x = x1 - i
    y = y1 - i
    z = ref_z - width_tunnel // 2
    range_y_air = range(y + 1, y + height_tunnel - 1)
    range_z_air = (z + 1, z + 2, z + 3)
    mc.build(x, range_y_air, range_z_air, air)
    if i%4==0:
        # Place torches down the right hand side of the tunnel
        mc.build(x, y + 1, ref_z + 1, torch)
# Send all blocks to minetest but send air and torches last to ensure tunnel is built
# before adding these extras. If air is sent before the glass then adjacent lava and water could
# flow into the void left by the air
mc.send_building((air,torch))



# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
