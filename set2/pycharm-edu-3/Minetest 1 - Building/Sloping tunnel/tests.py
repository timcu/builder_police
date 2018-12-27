# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018 - 2019

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_send_building, mock_create
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    # Location of end points of sloping section of tunnel (centre of floor)
    x1 = 69
    y1 = 14
    x2 = 9
    ref_z = player_z

    # Dimensions
    tunnel_height = 7
    tunnel_width = 5
    num_segments = x1 - x2 + 1

    # Building materials
    glass = "default:glass"
    floor = "default:stone"
    torch = "default:torch"
    air = "air"

    # Make the full tunnel in solid glass and stone first
    for i in range(num_segments):
        # Cross section of tunnel at position i
        # x, y, z are coordinates of lower left corner of segment of tunnel
        x = x1 - i
        y = y1 - i
        z = ref_z - tunnel_width // 2
        # Build 5 x 7 blocks of glass at position i for walls, roof, and centre
        range_y_ext = range(y, y + tunnel_height)
        range_z_ext = range(z, z + tunnel_width)
        b.update(nodebuilder.build(x, range_y_ext, range_z_ext, glass))
        # Build 3 x 1 blocks of stone at position i for floor
        range_z_floor = (z + 1, z + 2, z + 3)
        b.update(nodebuilder.build(x, y, range_z_floor, floor))
    # hollow out the tunnel because now we are sure that lava and water can't flow in the ends
    for i in range(num_segments):
        # Use air to hollow out the tunnel
        x = x1 - i
        y = y1 - i
        z = ref_z - tunnel_width // 2
        range_y_air = range(y + 1, y + tunnel_height - 1)
        range_z_air = (z + 1, z + 2, z + 3)
        b.update(nodebuilder.build(x, range_y_air, range_z_air, air))
        if i % 4 == 0:
            # Place torches down the right hand side of the tunnel
            b.update(nodebuilder.build(x, y + 1, ref_z + 1, torch))
    return b


def test_building():
    from task import mc
    return test_building_with_pattern(mc, building_pattern)


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
