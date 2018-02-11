from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel

mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

x1 = 93
x2 = 70
y = 14
z = 0

# build a solid cuboid of glass first which is 7 blocks high and 5 blocks wide
mc.set_nodes(x1, y  , z-2, x2, y+6, z+2, "default:glass")
# replace the internal glass with air so left with a hollow tunnel
mc.set_nodes(x1, y+1, z-1, x2, y+5, z+1, "air")









# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
