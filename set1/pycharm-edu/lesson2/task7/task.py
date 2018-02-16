# tunnel = procedure to build tunnel

from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
from minetest_helper import set_node, set_nodes, send_node_dict, build_station_dirx


mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)


def build_tunnel_dirx(minetest_connection, x1, x2, z, y1=None, y2=None, materials=None, floor=-55, tail=10, room=None):
    """Builds a tunnel in the x direction. Returns the node_dict

    minetest_connection should be the MinetestConnection object
    x1,x2 = tunnel goes from x = x1 to x = x2 excluding x1 and x2
    z = tunnel uses same position z for full length of tunnel
    y1,y2 = vertical position of base of tunnel at each end. If not provided then ground level is used
    materials: {             # see build_station_dirx for defaults
        'station_roof' : building material for roof
        'station_floor': building material for floor, platform and part of walls
        'station_door' : type of doors
        'station_stair': type of stairs
    }
    floor = minimum vertical position of tunnel
    tail = length of flat tunnel at each end
    room: {                  # see build_station_dirx for defaults
        'length': station waiting room length
        'width' : station waiting room width
        'height': station waiting room height
    }
    """
    nd = {}
    if x1 < x2:
        xmin, y_at_xmin, xmax, y_at_xmax = x1, y1, x2, y2
    else:
        xmin, y_at_xmin, xmax, y_at_xmax = x2, y2, x1, y1

    # xmin = x value at one end of tunnel.
    # xmax = x value at other end of tunnel. Must be greater than xmin
    # floor = minimum value of y for long tunnels
    # z = z position (same for full length of tunnel)
    # tail = length of horizontal at each end of tunnel

    # Define blocks
    stair_up_x = '{"name":"stairs:stair_stonebrick", "param2":"1"}'
    stair_dn_x = '{"name":"stairs:stair_stonebrick", "param2":"3"}'

    # First check we are not going to end up in a tree
    if not y_at_xmin:
        y_at_xmin = int(minetest_connection.get_ground_level(xmin, z))
    if not y_at_xmax:
        y_at_xmax = int(minetest_connection.get_ground_level(xmax, z))
    # Set a gold surveyors peg at endpoints of the tunnel
    # We don't build above here because by building we would move ground level and next time
    # we build it would build higher than previous build
    nd.update(set_node(xmin, y_at_xmin, z, "default:goldblock"))
    nd.update(set_node(xmax, y_at_xmax, z, "default:goldblock"))

    # constants for tunnel_y_pos function
    kx = (xmax + xmin + y_at_xmin - y_at_xmax) // 2
    ky = y_at_xmin + tail + xmin - kx
    if ky + 5 > floor:
        ymin = ky + 5  # short tunnels
    else:
        ymin = floor   # long tunnels

    # tunnel_y_pos returns a vertical position of the tunnel
    # for each value of the x position
    def tunnel_y_pos(x_pos):
        tunnel_y = abs(x_pos - kx) + ky
        if tunnel_y < ymin:
            return ymin
        if x_pos < kx:
            # tunnel floor should not be higher than y_at_xmin
            if tunnel_y > y_at_xmin:
                return y_at_xmin
        else:
            # tunnel floor should not be higher than y_at_xmax
            if tunnel_y > y_at_xmax:
                return y_at_xmax
        return tunnel_y

    # the z coordinate for the tunnel doesn't change for the full length

    # Initial loop to create a route made of solid glass with a stone base
    # Loop treats xmin and xmax as exclusive boundaries otherwise tunnel will keep
    # building on top of the last one each time you run it.
    for x in range(xmin+1, xmax):
        y = tunnel_y_pos(x)
        nd.update(set_nodes(x, y, z-2, x, y+6, z+2, "default:glass"))
        nd.update(set_nodes(x, y, z-1, x, y, z+1, "default:stone"))

    # Initialise previous value of y so can determine if stairs going up or down
    yprev = tunnel_y_pos(xmin+1)
    # Second loop to convert solid glass into a tunnel
    for x in range(xmin+2, xmax-1):
        y = tunnel_y_pos(x)
        # replace centre glass with air to make it a tunnel
        nd.update(set_nodes(x, y+1, z-1, x, y+5, z+1, "air"))
        # place a torch every 4 positions to light the tunnel
        # variation 5 = torch facing up
        # every 4 blocks
        # pos 0: powered RAIL and normal torch
        # pos 1: powered RAIL
        # pos 2: powered RAIL
        # pos 3: powered RAIL
        nd.update(set_node(x, y+1, z, "carts:powerrail"))
        if x % 4 == 0:
            nd.update(set_node(x, y+1, z+1, "default:torch"))
        # check if stairs are going up or down
        if y > yprev:
            # stairs ascending as x increases
            nd.update(set_node(x, y, z-1, stair_up_x))
        if y < yprev:
            # stairs descending as x increases
            nd.update(set_node(x-1, yprev, z-1, stair_dn_x))
        yprev = y

    # build station at xmax
    platform_length = tail-3
    platform_at_xmax = {
        'x': xmax - platform_length // 2 - 1,
        'y': y_at_xmax + 1,
        'z': z - 1,
        'length': platform_length
    }
    # Build a station at platform_at_xmax with 3 levels
    nd.update(build_station_dirx(platform_at_xmax, room=room, materials=materials, levels=3))

    # build station at xmin
    platform_at_xmin = {
        'x': xmin + platform_length // 2 + 2,
        'y': y_at_xmin + 1,
        'z': z - 1,
        'length': platform_length
    }
    # Build a station at platform_at_xmin with 1 level (the default)
    nd.update(build_station_dirx(platform_at_xmin, room=room, materials=materials))

    return nd
# build_tunnel_dirx finished


player_z = int(mc.send_cmd('get_player_z ' + mtuser))
# stations are too wide to be adjacent. Offset every second one by 50 in the x direction
x_offset = (player_z // 10 % 2) * 50
nd_tunnel = build_tunnel_dirx(mc, -300 + x_offset, -100 + x_offset, player_z)
send_node_dict(mc, nd_tunnel, end_list="air")


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
