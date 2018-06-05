from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# BUILDING LOCATION
# player's z coordinate used as reference point for all building
ref_z = player_z
# x value at start of stone path heading +x direction
path_x_min = 105
# y value of stone in path
floor_y = 9

# BUILDING SIZE
# height of arch in number of blocks (external dimension)
arch_height = 7
# width of arch in number of blocks (external dimension)
arch_width = 5
# path length
path_length = 16
# castle length (in x direction)
castle_length = 9
# castle width (in z direction)
castle_width = 5
# castle height excluding roof
castle_height = 4

# BUILDING MATERIALS
air = "air"
wall = "default:glass"
floor = "default:stone"
torch = "default:torch"

# ENGINEERING CALCULATIONS
# z value of side of arch (where wall_z < player_z)
wall_z = ref_z - arch_width // 2

# x value for arch location
range_x_arch = path_x_min

# external dimensions of arch
range_y_ext = range(floor_y, floor_y + arch_height)
range_z_ext = range(wall_z, wall_z + arch_width)
# internal dimensions of arch
range_y_int = range(floor_y + 1, floor_y + arch_height - 1)
range_z_int = range(wall_z + 1, wall_z + arch_width - 1)

# BUILD
# clear any existing structure or ground
mc.build(range(path_x_min, path_x_min + 40), range(floor_y + 1, floor_y + 31), range(ref_z - 4, ref_z + 5), air)
# build a solid cuboid of glass first which is 7 blocks high and 5 blocks wide
mc.build(range_x_arch, range_y_ext, range_z_ext, wall)
# replace the internal glass with air so left with a hollow tunnel
mc.build(range_x_arch, range_y_int, range_z_int, air)
# replace the floor with stone
mc.build(range_x_arch, floor_y, range_z_int, floor)
# place a torch in each arch
mc.build(range_x_arch, floor_y + 1, ref_z + 1, torch)



mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018.
