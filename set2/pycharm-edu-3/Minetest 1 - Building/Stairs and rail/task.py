from ircbuilder import open_irc
from ircbuilder.building import Building

from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z

b = Building()

# start point of tunnel
x1 = 69
x2 = 9
task4_x1 = 93
y1 = 14
z = player_z
num_segments = x1 - x2 + 1

# store node types in variables for easier use
stair_up_x = {"name": "stairs:stair_stonebrick", "direction": "+x"}
rail = 'carts:rail'
power_rail = 'carts:powerrail'

# sloping section of tunnel
for i in range(num_segments):
    # Add stairs - Don't need stairs on very last block. Hence check i < 60
    if i < 60:
        b.build(x1 - i, y1 - i, z - 1, stair_up_x)
    # Add power rail
    b.build(x1 - i, y1 - i + 1, z, power_rail)

# flat section of tunnel
for x in range(x1, task4_x1 + 1):
    # Add rail or power rail in pairs
    if x // 2 % 2 == 0:
        b.build(x, y1 + 1, z, rail)
    else:
        b.build(x, y1 + 1, z, power_rail)

with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel) as mc:
    b.send(mc)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
