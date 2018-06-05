# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_send_building, mock_create
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    ref_z = player_z
    wool = r"wool:(white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet)"
    # position of centre of diamond
    cx = 100
    cy = 32
    z = player_z

    # array of node types which we will alternate through
    colours = [wool, wool]

    # calculate extents of diamond
    width = 21
    height = 21
    x1 = cx - width // 2
    y1 = cy - height // 2
    x2 = x1 + width
    y2 = y1 + height
    b = nodebuilder.build(range(x1,x2),range(y1,y2),ref_z,"air")
    for y in range(y1,y2):
        # calculate x range which will give diamond shape
        xlo = x1 + abs(y - cy)
        xhi = x2 - abs(y - cy)
        for x in range(xlo,xhi):
            # set each node to an alternate wool colour by adding position to node list
            b.update(nodebuilder.build(x, y, z, colours[(x+y)%2]))
    return b


def test_building():
    from task import mc
    success = test_building_with_pattern(mc, building_pattern)
    if success:
        # Check no adjacent blocks the same
        keys=sorted(mc.building.keys())
        key_prev=(-100, -100, -100)
        wool_prev = ""
        for key in keys:
            wool = mc.building[key]
            if wool == wool_prev and abs(key[0]-key_prev[0]) < 2 and abs(key[1]-key_prev[1]) < 2:
                # adjacent the same so fail
                failed("Blocks at " + str(key_prev) + " and " + str(key) + " are adjacent but are both " + str(wool))
                return False
    return True


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


@mock.patch('ircbuilder.MinetestConnection.create', mock_create)
@mock.patch('ircbuilder.MinetestConnection.send_building', mock_send_building)
def run_patched_tests():
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_building()


if __name__ == '__main__':
    run_patched_tests()
