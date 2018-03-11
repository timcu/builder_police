from minetest_helper import set_node


def set_nodes(x1, y1, z1, x2, y2, z2, item):
    """similar to mc.set_nodes but stores nodes in node_dict rather than sending to minetest"""
    node_dict = {}
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1
    step_z = 1 if z2 > z1 else -1
    for z in range(z1, z2 + step_z, step_z):
        for y in range(y1, y2 + step_y, step_y):
            for x in range(x1, x2 + step_x, step_x):
                # Use the set_node function from the minetest_helper module
                node_dict.update(set_node(x, y, z, item))
    return node_dict


def node_lists_from_node_dict(node_dict):
    """Convert node_dict to node_lists"""
    node_lists = {}
    for pos, item in node_dict.items():
        if item not in node_lists:
            # Create a new list and store in node_lists with key=item
            node_lists[item] = []
        # Add pos to the end of the list with key=item in node_lists
        node_lists[item].append(pos)
    return node_lists


def send_node_lists(mc, node_lists, end_list=()):
    """ Send node_lists to minetest. Can specify order of items

    mc : MinetestConnection object
    node_lists : { 'item1':[(x1,y1,z1), ((x2a,y2a,z2a),(x2b,y2b,z2b)), ...], 'item2':[...]}
    end_list : ('air', 'door:') # User can choose the last items to be sent to minetest if order important
    """
    # User may have accidentally sent a str rather than a tuple or list for end_list
    # If so, convert to a tuple containing the str
    if isinstance(end_list, str):
        end_list = (end_list,)
    # Get the keys in a mutable (editable) form so we can rearrange the ones at the end
    item_list = list(node_lists.keys())
    # Rearrange the list
    for item in end_list:
        for key in item_list:
            if key.find(item) == 0:
                # pull key out of the list from its current position
                item_list.remove(key)
                # put key back in the list at the end
                item_list.append(key)
    # Send each node_list to minetest in the correct order
    for item in item_list:
        mc.set_node_list(node_lists[item], item)


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use at CoderDojo sessions in 2018.
