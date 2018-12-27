import math
import json


def build(x, y, z, item):
    """similar to MinetestConnection.set_node but stores nodes in node_dict rather than sending to minetest

    x, y, z: coordinates to be added to nodes. They are converted to integers so that each node has unique set of coordinates
    item: minetest item name as a string "default:glass", or json string '{"name":"default:torch", "param2":"1"}'

    returns node_dict: {(x1, y1, z1): item} Dictionary of node
    """
    x = math.floor(x+0.5)
    y = math.floor(y+0.5)
    z = math.floor(z+0.5)
    return {(x, y, z): item}


def build_cuboid(x1, y1, z1, x2, y2, z2, item):
    """similar to MinetestConnection.set_nodes but stores nodes in node_dict rather than sending to minetest"""
    node_dict = {}
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1
    step_z = 1 if z2 > z1 else -1
    for z in range(z1, z2 + step_z, step_z):
        for y in range(y1, y2 + step_y, step_y):
            for x in range(x1, x2 + step_x, step_x):
                node_dict.update(build(x, y, z, item))
    return node_dict


def node_lists_with_cuboids(node_lists_flat):
    """Finds adjacent points in node_lists_flat and converts them to cuboids for data efficiency"""
    node_lists = {}
    for item, v in node_lists_flat.items():
        node_lists[item] = []
        # v is a list of singular tuples for given item
        # vs is sorted in ascending order
        vs = sorted(v)
        # look for consecutive blocks in x then y then z
        while len(vs) > 0:
            start_x, start_y, start_z = vs[0]
            dx, dy, dz = 0, 0, 0
            tfx, tfy, tfz = True, True, True
            while tfx or tfy or tfz:
                if tfx:
                    x = start_x+dx+1
                    for y in range(start_y, start_y+dy+1):
                        for z in range(start_z, start_z+dz+1):
                            if not (x, y, z) in vs:
                                tfx = False
                    if tfx:
                        dx += 1
                if tfy:
                    y = start_y+dy+1
                    for x in range(start_x, start_x+dx+1):
                        for z in range(start_z, start_z+dz+1):
                            if not (x, y, z) in vs:
                                tfy = False
                    if tfy:
                        dy += 1
                if tfz:
                    z = start_z+dz+1
                    for x in range(start_x, start_x+dx+1):
                        for y in range(start_y, start_y+dy+1):
                            if not (x, y, z) in vs:
                                tfz = False
                    if tfz:
                        dz += 1
            if dx == 0 and dy == 0 and dz == 0:
                node_lists[item].append((start_x, start_y, start_z))
            else:
                node_lists[item].append(((start_x, start_y, start_z), (start_x+dx, start_y+dy, start_z+dz)))
                #print("Cuboid " + item + " " + str(((start_x, start_y, start_z), (start_x+dx, start_y+dy, start_z+dz))))
            for x in range(start_x, start_x+dx+1):
                for y in range(start_y, start_y+dy+1):
                    for z in range(start_z, start_z+dz+1):
                        vs.remove((x, y, z))
    return node_lists


def node_lists_from_node_dict(node_dict):
    """Convert node_dict to node_lists"""
    node_lists = {}
    for pos, item in node_dict.items():
        str_item = json.dumps(item) if isinstance(item, dict) else str(item)
        if str_item not in node_lists:
            node_lists[str_item] = []
        node_lists[str_item].append(pos)
    return node_lists_with_cuboids(node_lists)


def send_node_lists(mc, node_lists, end_list=()):
    """ Send node_lists to minetest. Should send air after walls so no lava and water flow in

    mc : MinetestConnection object
    node_lists : { 'item1':[(x1,y1,z1), ((x2a,y2a,z2a),(x2b,y2b,z2b)), ...], 'item2':[...]}
    end_list : ('air', 'door:')
    """
    item_list = list(node_lists.keys())
    if isinstance(end_list, str):
        end_list = (end_list,)
    for item in end_list:
        for key in item_list:
            if key.find(item) == 0:
                item_list.remove(key)
                item_list.append(key)
    for item in item_list:
        mc.set_node_list(node_lists[item], item)


def send_node_dict(mc, node_dict, end_list=()):
    """Convert node_dict to node_lists and send to minetest

    mc : MinetestConnection object
    node_dict : { (x1,y1,z1):'item1', (x2,y2,z2):'item2', ...}
    end_list : ('air', 'door:')
    """
    node_lists = node_lists_from_node_dict(node_dict)
    send_node_lists(mc, node_lists, end_list)


def build_station_dirx(platform, room=None, materials=None, levels=1):
    """Build an direction_x running platform and station next to a direction_x tunnel. Returns the node_dict

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
    nd.update(build_cuboid(platform_x1, platform_y, platform_z, platform_x2, platform_y, platform_z, floor))
    nd.update(build(platform_x1 - 1, platform_y, platform_z, stair_up_x))
    nd.update(build(platform_x2 + 1, platform_y, platform_z, stair_dn_x))
    # station waiting room with levels
    # first make a solid box of floor material
    nd.update(build_cuboid(station_x1, platform_y, station_z1, station_x2, platform_y + (1 + room_height) * levels - 1, station_z2, floor))
    # make windows and a room on each level
    for level in range(0, levels):
        nd.update(build_cuboid(station_x1, platform_y + (1 + room_height) * level + 2, station_z1, station_x2, platform_y + (1 + room_height) * level + room_height - 1, station_z2, "default:glass"))
        nd.update(build_cuboid(station_x1 + 1, platform_y + (1 + room_height) * level + 1, station_z1 + 1, station_x2 - 1, platform_y + (1 + room_height) * level + room_height, station_z2 - 1, "air"))
    # stairs between levels
    stair_z = station_z2 - 1
    for y in range(0, (levels-1)*(room_height + 1)):
        stair_y = y + platform_y + 1
        stair_x = station_x2 - 2 - y % (room_height + 1)
        nd.update(build(stair_x, stair_y, stair_z, stair_dn_x))
        nd.update(build_cuboid(stair_x, stair_y + 1, stair_z, stair_x, stair_y + 4, stair_z, "air"))
    # open the station to platform
    nd.update(build_cuboid(platform_x1, platform_y + 1, station_z2, platform_x2, platform_y + tunnel_height - 1, station_z2+1, "air"))
    # Roof
    roof_layer = 0
    layer_width = station_width + 2 - 2 * roof_layer
    roof_x1 = station_x1-1
    roof_x2 = station_x2+1
    while layer_width > 0:
        roof_y = platform_y + (room_height + 1) * levels + roof_layer
        roof_z2 = station_z2 + 1 - roof_layer
        roof_z1 = roof_z2 - layer_width + 1
        nd.update(build_cuboid(roof_x1, roof_y, roof_z1, roof_x2, roof_y, roof_z2, roof))
        roof_layer += 1
        layer_width = station_width + 2 - 2 * roof_layer
    # doors
    nd.update(build(platform['x'] + 1, platform_y + 2, station_z1, "air"))
    nd.update(build(platform['x'], platform_y + 2, station_z1, "air"))
    nd.update(build(platform['x'] + 1, platform_y + 1, station_z1, door_left))
    nd.update(build(platform['x'], platform_y + 1, station_z1, door_right))
    # make a walkway around the outside of the doors
    nd.update(build_cuboid(station_x1, platform_y, station_z1-1, station_x2, platform_y, station_z1-1, floor))
    nd.update(build_cuboid(station_x1, platform_y+1, station_z1-1, station_x2, platform_y + room_height, station_z1-1, "air"))
    return nd
# build_station_dirx finished


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
    nd.update(build(xmin, y_at_xmin, z, "default:goldblock"))
    nd.update(build(xmax, y_at_xmax, z, "default:goldblock"))

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
        nd.update(build_cuboid(x, y, z-2, x, y+6, z+2, "default:glass"))
        nd.update(build_cuboid(x, y, z-1, x, y, z+1, "default:stone"))

    # Initialise previous value of y so can determine if stairs going up or down
    yprev = tunnel_y_pos(xmin+1)
    # Second loop to convert solid glass into a tunnel
    for x in range(xmin+2, xmax-1):
        y = tunnel_y_pos(x)
        # replace centre glass with air to make it a tunnel
        nd.update(build_cuboid(x, y+1, z-1, x, y+5, z+1, "air"))
        # place a torch every 4 positions to light the tunnel
        # variation 5 = torch facing up
        # every 4 blocks
        # pos 0: powered RAIL and normal torch
        # pos 1: powered RAIL
        # pos 2: powered RAIL
        # pos 3: powered RAIL
        nd.update(build(x, y+1, z, "carts:powerrail"))
        if x % 4 == 0:
            nd.update(build(x, y+1, z+1, "default:torch"))
        # check if stairs are going up or down
        if y > yprev:
            # stairs ascending as x increases
            nd.update(build(x, y, z-1, stair_up_x))
        if y < yprev:
            # stairs descending as x increases
            nd.update(build(x-1, yprev, z-1, stair_dn_x))
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
