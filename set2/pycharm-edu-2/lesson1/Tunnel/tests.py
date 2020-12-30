# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_building_send, mock_create
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    ref_z = player_z
    b = {}
    # glass = "default:glass"
    # wool = r"wool:(white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet)"
    air = "air"
    wall = "default:glass"
    # BUILDING LOCATION
    x_max = 93
    x_min = 70
    floor_y = 14
    # BUILDING SIZE
    tunnel_height = 7
    tunnel_width = 5
    # ENGINEERING CALCULATIONS
    tunnel_length = x_max - x_min + 1
    wall_z = player_z - tunnel_width // 2
    range_x = range(x_min, x_min + tunnel_length)
    range_y_ext = range(floor_y, floor_y + tunnel_height)
    range_z_ext = range(wall_z, wall_z + tunnel_width)
    range_y_int = range(floor_y + 1, floor_y + tunnel_height - 1)
    range_z_int = range(wall_z + 1, wall_z + tunnel_width - 1)
    # BUILD
    b.update(nodebuilder.build(range_x, range_y_ext, range_z_ext, wall))
    # replace the internal glass with air so left with a hollow tunnel
    b.update(nodebuilder.build(range_x, range_y_int, range_z_int, air))
    return b


def test_building():
    from task import b
    return test_building_with_pattern(b, building_pattern)


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


@mock.patch('ircbuilder.MinetestConnection.create', mock_create)
@mock.patch('ircbuilder.building.Building.send', mock_building_send)
def run_patched_tests():
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_building()


if __name__ == '__main__':
    run_patched_tests()
