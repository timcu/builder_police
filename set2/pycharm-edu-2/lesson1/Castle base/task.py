from ircbuilder import open_irc
from ircbuilder.building import Building

from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# BUILDING LOCATION
# player's z coordinate used as reference point for all building
ref_z = player_z
# x value at start of stone path heading +x direction
path_x_min = 105
# x value at start of castle
castle_x_min = 121
# y value of floor of castle
floor_y = 9

# BUILDING SIZE
# castle length (in x direction)
castle_length = 9
# castle width (in z direction)
castle_width = 5
# castle height excluding roof including floor
castle_height = 5

# BUILDING MATERIALS
air = "air"
castle = "default:stone"

# ENGINEERING CALCULATIONS
# z value of side of castle (where castle_wall_z < player_z)
wall_z = ref_z - castle_width // 2
# external dimensions of castle base
range_x_castle_ext = range(castle_x_min, castle_x_min + castle_length)
range_y_castle_ext = range(floor_y, floor_y + castle_height)
range_z_castle_ext = range(wall_z, wall_z + castle_width)
# internal dimensions of castle base
range_x_castle_int = range(castle_x_min + 1, castle_x_min + castle_length - 1)
range_y_castle_int = range(floor_y + 1, floor_y + castle_height)
range_z_castle_int = range(wall_z + 1, wall_z + castle_width - 1)

# BUILD
# clear any existing structure or ground
b.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(ref_z - 4, ref_z + 5), air)
# the base of the castle
b.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle)
b.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air)
# create a doorway
b.build(castle_x_min, [floor_y + 1, floor_y + 2], ref_z, air)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
