from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# BUILDING LOCATION
ref_z = player_z
x_max = number
x_min = number
floor_y = number

# BUILDING SIZE
tunnel_height = number
tunnel_width = number

# BUILDING MATERIALS
air = "air"
wall = "default:glass"

# ENGINEERING CALCULATIONS
tunnel_length = x_max - x_min + 1

wall_z = ref_z - tunnel_width // 2
# x values for tunnel glass and air
range_x = range(x_min, x_min + tunnel_length)
# y and z values for glass on exterior of tunnel
range_y_ext = sequence
range_z_ext = sequence
# y and z values for air in the interior of tunnel
range_y_int = range(floor_y + 1, floor_y + tunnel_height - 1)
range_z_int = range(wall_z + 1, wall_z + tunnel_width - 1)

# BUILD
# build a solid cuboid of glass first which is 7 blocks high and 5 blocks wide
mc.build(range_x, variable, range_z_ext, wall)
# replace the internal glass with air so left with a hollow tunnel
mc.build(range_x, range_y_int, variable, air)

mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2019.
