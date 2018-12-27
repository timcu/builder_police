import math

# Create a new dictionary for node_dict
node_dict = {}

# Set block at x=15, y=20, z=10 to "default:wood" using a tuple for the x, y, z coordinates
node_dict[(15, 20, 10)] = "default:wood"
print("A:", node_dict)

# Set block at x=16, y=20, z=10 to "default:glass"
node_dict[(16, 20, 10)] = "default:glass"
print("B:", node_dict)

# Set two blocks at x=16, y=20, z=10 and z=11 to "default:stone"
for z in range(10,12):
    node_dict[(16, 20, z)] = "default:stone"
print("C:", node_dict)

# Set coordinates in variables at x=15 y=20, z=10.1
x = 15
y = 20
z = 10.1
# Set block at x, y, z to "wool:blue"
node_dict[(x, y, z)] = "wool:blue"
print("D:", node_dict)

# Remove node at x, y, z
del(node_dict[(x, y, z)])
print("E:", node_dict)

# Use a formula to convert float to int coordinates of the centre of the node
# Use one of the four formulae in the test below (or make up your own)
node_dict[(x, y, math.floor(z + 0.5))] = "wool:blue"
print("F:", node_dict)

# Test four formulae to see which is best for converting float to centre of node
print()
print("Test four formulae")
print("  z       f1     f2     f3     f4")
print("=================================")
for i in range(-24, 25, 2):
    z = i / 10
    f1 = int(z)
    f2 = math.floor(z)
    f3 = int(z + 0.5)
    f4 = math.floor(z + 0.5)
    print("{: .2f}     {: d}     {: d}     {: d}     {: d}".format(z, f1, f2, f3, f4))


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use in schools and CoderDojo sessions in 2018 - 2019.
