from ircbuilder import MinetestConnection
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z
from math import sqrt


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

# LOCATION
ref_z = player_z
pole_x = 122
pole_y = 15
flag_y = 22

# SIZE
flag_height = 13
flag_length = 21

# SHAPE

def rectangle_flag(global_x, global_y):
    local_x = global_x - pole_x
    local_y = global_y - flag_y
    if local_x < 0 or local_x >= flag_length:
        return False
    if local_y < 0 or local_y >= flag_height:
        return False
    return True


def top_triangle_flag(global_x, global_y):
    local_x = global_x - pole_x
    local_y = global_y - flag_y
    row_length = flag_length * local_y // flag_height + 1
    if local_x < 0 or local_x >= row_length:
        return False
    if local_y < 0 or local_y >= flag_height:
        return False
    return True


def half_ellipse_flag(global_x, global_y):
    local_x = global_x - pole_x
    local_y = global_y - flag_y
    if local_y < 0 or local_y >= flag_height:
        return False
    if local_x == 0:
        return True
    y = local_y - flag_height // 2
    x = local_x
    r2 = (x / flag_length) ** 2 + (2 * y / flag_height) ** 2
    return r2 <= 1.0


# BUILDING MATERIALS
air = "air"
pole = "default:fence_junglewood"
colours = ["wool:" + colour for colour in "white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet".split("|")]

# ENGINEERING CALCULATIONS
num_colours = len(colours)
stripe_width = 5

mc.build(pole_x, range(pole_y, flag_y), ref_z, pole)
mc.build(range(pole_x, pole_x + 26), range(flag_y, flag_y + 26), range(ref_z - 4, ref_z + 5), air)
for x in range(pole_x, pole_x + flag_length):
    for y in range(flag_y, flag_y + flag_height):
        # pattern centred on centre of flag
        cx = pole_x + flag_length / 2
        cy = flag_y + flag_height / 2
        # pattern centred on front bottom corner
        # cx = pole_x
        # cy = flag_y

        c = x // 2 % 15  # vertical stripes
        # c = y // 2 % 15  # horizontal stripes
        # c = (x+y)//2 % 15  # diagonal stripes
        # c = (x-y)//2 % 15  # other diagonal stripes
        # c = int(sqrt((x-cx)**2 + (y-cy)**2) ) // stripe_width % num_colours  #  circles centred on cx, cy
        # c = int(max(abs(x-cx), abs(y-cy))) % len(colours)  # squares centred on cx, cy
        # c = int(min(abs(x-cx), abs(y-cy))) % len(colours)  # cross centred on cx, cy
        colour = colours[c]
        if rectangle_flag(x, y):
            mc.build(x, y, ref_z, colour)
        else:
            mc.build(x, y, ref_z, "air")


mc.send_building()


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at schools and CoderDojo in 2018 - 2019.
