from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

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
# player looking in x direction to look through this window
window_x = {"name":"xpanes:bar_flat", "direction":"+x"}
# player looking in z direction to look through this window
window_z = {"name":"xpanes:bar_flat", "direction":"+z"}
# player looking in x direction to climb this ladder.
ladder = {"name":"default:ladder_wood","direction":"+x"}
carpet = "wool:red"
# direction specifies which way player is facing when opening door.
door = {"name":"doors:door_wood_a", "direction":"+x"}
# torches. Direction specifies which way player facing to view torch
torch_n = {"name":"default:torch_wall", "direction":"-z"}
torch_s = {"name":"default:torch_wall", "direction":"+z"}


# ENGINEERING CALCULATIONS
# z values of sides of castle
wall_z1 = ref_z - castle_width // 2
wall_z2 = ref_z + castle_width // 2
# external dimensions of castle base
range_x_castle_ext = range(castle_x_min, castle_x_min + castle_length)
range_y_castle_ext = range(floor_y, floor_y + castle_height)
range_z_castle_ext = range(wall_z1, wall_z1 + castle_width)
# internal dimensions of castle base
range_x_castle_int = range(castle_x_min + 1, castle_x_min + castle_length - 1)
range_y_castle_int = range(floor_y + 1, floor_y + castle_height)
range_z_castle_int = range(wall_z1 + 1, wall_z1 + castle_width - 1)
# height of side windows from 2 above floor to height of castle
range_y_window = range(floor_y + 2, floor_y + castle_height)
# place side windows every 2 blocks starting from second block from door
range_x_window = range(castle_x_min + 2, castle_x_min + castle_length - 2, 2)
# external dimensions of castle roof
range_x_roof_ext = range(castle_x_min - 1, castle_x_min + castle_length + 1)
range_y_roof_ext = range(floor_y + castle_height, floor_y + castle_height + 3)
range_z_roof_ext = range(wall_z1 - 1, wall_z1 + castle_width + 1)
range_x_roof_int = range_x_castle_ext
range_y_roof_int = range(floor_y + castle_height + 1, floor_y + castle_height + 3)
range_z_roof_int = range_z_castle_ext
# location of crenels and merlons on castle roof
crenel_y = floor_y + castle_height + 2
roof_x1 = castle_x_min - 1
roof_x2 = castle_x_min + castle_length
roof_z1 = wall_z1 - 1
roof_z2 = wall_z2 + 1

# BUILD
# clear any existing structure or ground
mc.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(ref_z - 4, ref_z + 5), air)
# the base of the castle
mc.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle)
mc.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air)
# create a doorway
mc.build(castle_x_min, [floor_y + 1, floor_y + 2], ref_z, air)
# add windows on side walls
mc.build(range_x_window, range_y_window, (wall_z1, wall_z2), window_z)
# add windows on front wall
mc.build(castle_x_min, floor_y + 4, (ref_z - 1, ref_z, ref_z + 1), window_x)
# the roof of the castle
mc.build(range_x_roof_ext, range_y_roof_ext, range_z_roof_ext, castle)
mc.build(range_x_roof_int, range_y_roof_int, range_z_roof_int, air)
# build the ladder. Has to be against wall for player to climb it easily.
mc.build(castle_x_min + castle_length - 2, range(floor_y + 1, floor_y + castle_height + 1), ref_z, ladder)
# build crenels on roof
mc.build((roof_x1, roof_x2), crenel_y, range(wall_z1, wall_z1 + castle_width, 2), air)
mc.build(range(castle_x_min, castle_x_min + castle_length, 2), crenel_y, (roof_z1, roof_z2), air)
# build a door
mc.build(castle_x_min, floor_y + 1, ref_z, door)
# lay the red carpet
mc.build(range(path_x_min, castle_x_min + castle_length - 1), floor_y, ref_z, carpet)
# torches
mc.build(range(castle_x_min + 1, castle_x_min + castle_length - 1, 2), floor_y + 3, wall_z1 + 1, torch_n)
mc.build(range(castle_x_min + 1, castle_x_min + castle_length - 1, 2), floor_y + 3, wall_z2 - 1, torch_s)

mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018.
