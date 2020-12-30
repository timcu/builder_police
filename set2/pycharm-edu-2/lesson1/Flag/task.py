from ircbuilder import open_irc
from ircbuilder.building import Building
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z
from math import sqrt


b = Building()

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
    centre_y = local_y - flag_height // 2
    centre_x = local_x
    r2 = (centre_x / flag_length) ** 2 + (2 * centre_y / flag_height) ** 2
    return r2 <= 1.0


# BUILDING MATERIALS
air = "air"
pole = "default:fence_junglewood"
colours = ["wool:" + colour for colour in "white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet".split("|")]

# ENGINEERING CALCULATIONS
num_colours = len(colours)
stripe_width = 2

b.build(pole_x, range(pole_y, flag_y), ref_z, pole)
b.build(range(pole_x, pole_x + 26), range(flag_y, flag_y + 26), range(ref_z - 4, ref_z + 5), air)
for x in range(pole_x, pole_x + flag_length):
    for y in range(flag_y, flag_y + flag_height):
        # pattern centred on centre of flag
        cx = pole_x + flag_length / 2
        cy = flag_y + flag_height / 2
        # pattern centred on front bottom corner
        # cx = pole_x
        # cy = flag_y

        # c = x  # vertical stripes
        # c = y  # horizontal stripes
        # c = (x + y)  # diagonal stripes
        # c = (x - y)  # other diagonal stripes
        c = int(sqrt((x - cx)**2 + (y - cy)**2))  # circles centred on cx, cy
        # c = int(max(abs(x - cx), abs(y - cy)))  # squares centred on cx, cy
        # c = int(min(abs(x - cx), abs(y - cy)))  # cross centred on cx, cy
        colour = colours[c // stripe_width % num_colours]
        if rectangle_flag(x, y):
            b.build(x, y, ref_z, colour)
        else:
            b.build(x, y, ref_z, "air")

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
