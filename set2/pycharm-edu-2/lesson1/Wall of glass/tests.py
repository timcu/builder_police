# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_send_building, mock_create
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    # BUILDING MATERIALS
    air = "air"
    wall = "default:glass"
    # BUILDING LOCATION
    path_x_min = 105
    floor_y = 9
    # BUILDING SIZE
    arch_height = 7
    arch_width = 5
    # ENGINEERING CALCULATIONS
    wall_z = player_z - arch_width // 2
    range_x_arch = path_x_min
    range_y_ext = range(floor_y, floor_y + arch_height)
    range_z_ext = range(wall_z, wall_z + arch_width)
    # BUILD
    b.update(nodebuilder.build(range(path_x_min, path_x_min + 40), range(floor_y + 1, floor_y + 31), range(player_z - 4, player_z + 5), air))
    b.update(nodebuilder.build(range_x_arch, range_y_ext, range_z_ext, wall))
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
