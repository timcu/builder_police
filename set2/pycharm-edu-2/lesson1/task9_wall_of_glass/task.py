from ircbuilder import open_irc
from ircbuilder.building import Building

from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

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

# BUILDING MATERIALS
air = "air"
wall = "default:glass"

# ENGINEERING CALCULATIONS
# z value of side of arch (where wall_z < player_z)
wall_z = ref_z - arch_width // 2
# x value for arch location
range_x_arch = path_x_min
# external dimensions of arch
range_y_ext = range(floor_y, floor_y + arch_height)
range_z_ext = range(wall_z, wall_z + arch_width)

# BUILD
# clear any existing structure or ground
b.build(range(path_x_min, path_x_min + 40), range(floor_y, floor_y + 31), range(ref_z - 4, ref_z + 5), air)
b.build(range(path_x_min, path_x_min + 16), floor_y, range(ref_z - 1, ref_z + 2), "default:stone")
# build a solid cuboid of glass first which is 7 blocks high and 5 blocks wide
b.build(range_x_arch, range_y_ext, range_z_ext, wall)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
