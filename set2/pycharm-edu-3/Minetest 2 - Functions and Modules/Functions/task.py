import math


def build(x, y, z, item):
    """similar to MinetestConnection.set_node but stores nodes in a dictionary rather than sending to minetest

    x, y, z: coordinates to be added to nodes. They are converted to integers so that each node has unique set of coordinates
    item: minetest item name as a string "default:glass", or json string '{"name":"default:torch", "param2":"1"}'
    """
    x = math.floor(x+0.5)
    y = math.floor(y+0.5)
    z = math.floor(z+0.5)
    return {(x, y, z): item}


# Create a new dictionary for node_dict
node_dict = {}

# Set block at x=15, y=20, z=10 to "default:wood" using a tuple for the x, y, z coordinates
node_dict.update(build(15, 20, 10, "default:wood"))
print("A:", node_dict)

# Set block at x=16, y=20, z=10 to "default:glass"
node_dict.update(build(16, 20, 10, "default:glass"))
print("B:", node_dict)

# Set two blocks at x=16, y=20, z=10 and z=11 to "default:stone"
for z in range(10,12):
    node_dict.update(build(16, 20, z, "default:stone"))
print("C:", node_dict)

# Set coordinates in variables at x=15 y=20, z=10.1
x = 15
y = 20
z = 10.1
# Set block at x, y, z to "wool:blue"
node_dict.update(build(x, y, z, "wool:blue"))
print("D:", node_dict)


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
