# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_send_building, mock_create
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
    window_x = {'name':"xpanes:bar_flat", 'direction':r'(\+|\-)x'}
    window_z = {'name':"xpanes:bar_flat", 'direction':r'(\+|\-)z'}
    ladder = {"name":"default:ladder_wood","direction":r"\+x"}
    # ENGINEERING CALCULATIONS
    wall_z1 = player_z - castle_width // 2
    wall_z2 = player_z + castle_width // 2
    range_x_castle_ext = range(castle_x_min, castle_x_min + castle_length)
    range_y_castle_ext = range(floor_y, floor_y + castle_height)
    range_z_castle_ext = range(wall_z1, wall_z1 + castle_width)
    range_x_castle_int = range(castle_x_min + 1, castle_x_min + castle_length - 1)
    range_y_castle_int = range(floor_y + 1, floor_y + castle_height)
    range_z_castle_int = range(wall_z1 + 1, wall_z1 + castle_width - 1)
    range_y_window = range(floor_y + 2, floor_y + castle_height)
    range_x_window = range(castle_x_min + 2, castle_x_min + castle_length - 2, 2)
    range_x_roof_ext = range(castle_x_min - 1, castle_x_min + castle_length + 1)
    range_y_roof_ext = range(floor_y + castle_height, floor_y + castle_height + 3)
    range_z_roof_ext = range(wall_z1 - 1, wall_z1 + castle_width + 1)
    range_x_roof_int = range_x_castle_ext
    range_y_roof_int = range(floor_y + castle_height + 1, floor_y + castle_height + 3)
    range_z_roof_int = range_z_castle_ext
    # BUILD
    b.update(nodebuilder.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(player_z - 4, player_z + 5), air))
    b.update(nodebuilder.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle))
    b.update(nodebuilder.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air))
    b.update(nodebuilder.build(castle_x_min, [floor_y + 1, floor_y + 2], player_z, air))
    b.update(nodebuilder.build(range_x_window, range_y_window, (wall_z1, wall_z2), window_z))
    b.update(nodebuilder.build(castle_x_min, floor_y + 4, (player_z - 1, player_z, player_z + 1), window_x))
    b.update(nodebuilder.build(range_x_roof_ext, range_y_roof_ext, range_z_roof_ext, castle))
    b.update(nodebuilder.build(range_x_roof_int, range_y_roof_int, range_z_roof_int, air))
    b.update(nodebuilder.build(castle_x_min + castle_length - 2, range(floor_y + 1, floor_y + castle_height + 1), player_z, ladder))
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
