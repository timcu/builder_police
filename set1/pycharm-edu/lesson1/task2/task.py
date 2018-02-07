from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser,mtuserpass, mtbotnick, channel
mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)

x = 100
y = 14
z = 20

mc.set_node(x, y-1, z-1, "default:glass")
mc.set_node(x, y-1, z  , "default:glass")
mc.set_node(x, y-1, z+1, "default:glass")
mc.set_node(x, y  , z-1, "default:glass")
mc.set_node(x, y  , z+1, "default:glass")
mc.set_node(x, y+1, z-1, "default:glass")
mc.set_node(x, y+1, z  , "default:glass")
mc.set_node(x, y+1, z+1, "default:glass")
mc.set_node(x, y, z, "wool:orange")






# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
