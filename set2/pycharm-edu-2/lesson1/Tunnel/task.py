from ircbuilder import open_irc
from ircbuilder.building import Building
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# BUILDING LOCATION
ref_z = player_z
x_max = 93
x_min = 70
floor_y = 14

# BUILDING SIZE
tunnel_height = 7
tunnel_width = 5

# BUILDING MATERIALS
air = "air"
wall = "default:glass"

# ENGINEERING CALCULATIONS
tunnel_length = x_max - x_min + 1

wall_z = ref_z - tunnel_width // 2
# x values for tunnel glass and air
range_x = range(x_min, x_min + tunnel_length)
# y and z values for glass on exterior of tunnel
range_y_ext = range(floor_y, floor_y + tunnel_height)
range_z_ext = range(wall_z, wall_z + tunnel_width)
# y and z values for air in the interior of tunnel
range_y_int = range(floor_y + 1, floor_y + tunnel_height - 1)
range_z_int = range(wall_z + 1, wall_z + tunnel_width - 1)

# BUILD
# build a solid cuboid of glass first which is 7 blocks high and 5 blocks wide
b.build(range_x, range_y_ext, range_z_ext, wall)
# replace the internal glass with air so left with a hollow tunnel
b.build(range_x, range_y_int, range_z_int, air)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
