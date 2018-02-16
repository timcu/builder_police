from minetest_helper import set_node, set_nodes, send_node_dict
from ircbuilder import MinetestConnection
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel


def build_station_dirx(platform, room=None, materials=None, levels=1):
    """Build an direction_x running platform and station next to a direction_x tunnel

    platform: {
        'x': x position of centre of platform
        'y': y position of centre of platform
        'z': z position of centre of platform
        'length': length of platform (default=10)
    }
    room: {
        'length': length of side of waiting room parallel to platform, excluding walls (default=20)
        'width' : length of side of waiting room perpendicular to platform, excluding walls (default=7)
        'height': height of room excluding floor and ceiling (default=5) (min=2)
    }
    materials: {
        'station_roof' : building material for roof (default:wood)
        'station_floor': building material for floor, platform and part of walls (default:wood)
        'station_door' : type of doors (doors:door_wood_a)
        'station_stair': type of stairs (stairs:stair_wood)
    }
    levels: number of stories high for station

    The only required data is platform with x, y, z coordinates (length is optional)
    """
    platform_length = platform['length'] if 'length' in platform else 10
    # Following will raise KeyError exception if 'x', 'y' or 'z' not in platform
    platform_x1 = platform['x'] - platform_length // 2
    platform_x2 = platform_x1 + platform_length - 1
    platform_y = platform['y']
    platform_z = platform['z']

    if not room:
        room = {}
    room_length = room['length'] if 'length' in room else 20
    room_width = room['width'] if 'width' in room else 7
    room_height = room['height'] if 'height' in room else 5

    if not materials:
        materials = {}
    roof = materials['station_roof'] if 'station_roof' in materials else 'default:wood'
    floor = materials['station_floor'] if 'station_floor' in materials else 'default:wood'
    door = materials['station_door'] if 'station_door' in materials else 'doors:door_wood_a'
    stair = materials['station_stair'] if 'station_stair' in materials else 'stairs:stair_wood'

    # ensure room height is at least 2 otherwise doors won't fit
    if room_height < 2:
        room_height = 2
    # ensure room is long enough to fit stairs (only required when more than one level)
    if levels > 1 and room_length < room_height + 3:
        room_length = room_height + 3
    # internal tunnel height
    tunnel_height = 5
    # external dimensions
    station_length = room_length + 2
    station_width = room_width + 2

    station_x1 = platform_x1 - (station_length - platform_length) // 2
    station_x2 = station_x1 + station_length - 1
    station_z2 = platform_z - 1
    station_z1 = station_z2 - station_width + 1

    stair_up_x = '{"name":"' + stair + '", "param2":"1"}'
    stair_dn_x = '{"name":"' + stair + '", "param2":"3"}'

    if door[-2:] in ('_a', '_b'):
        door = door[:-2]
    door_left = '{"name":"' + door + '_a","param2":"2"}'
    door_right = '{"name":"' + door + '_b","param2":"2"}'

    # platform with stairs at each end of platform
    nd = {}
    nd.update(set_nodes(platform_x1, platform_y, platform_z, platform_x2, platform_y, platform_z, floor))
    nd.update(set_node(platform_x1 - 1, platform_y, platform_z, stair_up_x))
    nd.update(set_node(platform_x2 + 1, platform_y, platform_z, stair_dn_x))
    # station waiting room with levels
    # first make a solid box of floor material
    nd.update(set_nodes(station_x1, platform_y, station_z1, station_x2, platform_y + (1 + room_height) * levels - 1, station_z2, floor))
    # make windows and a room on each level
    for level in range(0, levels):
        nd.update(set_nodes(station_x1, platform_y + (1 + room_height) * level + 2, station_z1, station_x2, platform_y + (1 + room_height) * level + room_height - 1, station_z2, "default:glass"))
        nd.update(set_nodes(station_x1 + 1, platform_y + (1 + room_height) * level + 1, station_z1 + 1, station_x2 - 1, platform_y + (1 + room_height) * level + room_height, station_z2 - 1, "air"))
    # stairs between levels
    stair_z = station_z2 - 1
    for y in range(0, (levels-1)*(room_height + 1)):
        stair_y = y + platform_y + 1
        stair_x = station_x2 - 2 - y % (room_height + 1)
        nd.update(set_node(stair_x, stair_y, stair_z, stair_dn_x))
        nd.update(set_nodes(stair_x, stair_y + 1, stair_z, stair_x, stair_y + 4, stair_z, "air"))
    # open the station to platform
    nd.update(set_nodes(platform_x1, platform_y + 1, station_z2, platform_x2, platform_y + tunnel_height - 1, station_z2+1, "air"))
    # Roof
    roof_layer = 0
    layer_width = station_width + 2 - 2 * roof_layer
    roof_x1 = station_x1-1
    roof_x2 = station_x2+1
    while layer_width > 0:
        roof_y = platform_y + (room_height + 1) * levels + roof_layer
        roof_z2 = station_z2 + 1 - roof_layer
        roof_z1 = roof_z2 - layer_width + 1
        nd.update(set_nodes(roof_x1, roof_y, roof_z1, roof_x2, roof_y, roof_z2, roof))
        roof_layer += 1
        layer_width = station_width + 2 - 2 * roof_layer
    # doors
    nd.update(set_node(platform['x'] + 1, platform_y + 2, station_z1, "air"))
    nd.update(set_node(platform['x'], platform_y + 2, station_z1, "air"))
    nd.update(set_node(platform['x'] + 1, platform_y + 1, station_z1, door_left))
    nd.update(set_node(platform['x'], platform_y + 1, station_z1, door_right))
    # make a walkway around the outside of the doors
    nd.update(set_nodes(station_x1, platform_y, station_z1-1, station_x2, platform_y, station_z1-1, floor))
    nd.update(set_nodes(station_x1, platform_y+1, station_z1-1, station_x2, platform_y + room_height, station_z1-1, "air"))
    return nd
# build_station_dirx finished


# The following code is to set up parameters to run build_station_dirx and then send node_dict to minetest
mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)
player_z = int(mc.send_cmd('get_player_z ' + mtuser))
# stations are too wide to be adjacent to each other. Offset every second one by 50 in the x direction
x_offset = (player_z // 10 % 2) * 50
xmax = -100 + x_offset
platform_length = 10
y_at_xmax = int(mc.get_ground_level(xmax, player_z))
platform_at_xmax = {
    'x': xmax - platform_length // 2 - 1,
    'y': y_at_xmax + 1,
    'z': player_z - 1,
    'length': platform_length
}
print(platform_at_xmax)
nd_station = build_station_dirx(platform_at_xmax, levels=3)
send_node_dict(mc, nd_station, ("air"))


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
