# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_building_send, mock_create
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    path_x_min = 105
    castle_x_min = 121
    floor_y = 9
    # BUILDING SIZE
    castle_length = 9
    castle_width = 5
    castle_height = 5
    # BUILDING MATERIALS
    air = "air"
    castle = "default:stone"
    # ENGINEERING CALCULATIONS
    wall_z = player_z - castle_width // 2
    range_x_castle_ext = range(castle_x_min, castle_x_min + castle_length)
    range_y_castle_ext = range(floor_y, floor_y + castle_height)
    range_z_castle_ext = range(wall_z, wall_z + castle_width)
    range_x_castle_int = range(castle_x_min + 1, castle_x_min + castle_length - 1)
    range_y_castle_int = range(floor_y + 1, floor_y + castle_height)
    range_z_castle_int = range(wall_z + 1, wall_z + castle_width - 1)
    # BUILD
    b.update(nodebuilder.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(player_z - 4, player_z + 5), air))
    b.update(nodebuilder.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle))
    b.update(nodebuilder.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air))
    b.update(nodebuilder.build(castle_x_min, [floor_y + 1, floor_y + 2], player_z, air))
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
