# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, mock_create, mock_building_send, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    castle_x_min = 121
    floor_y = 9
    # BUILDING SIZE
    castle_length = 9
    castle_width = 5
    castle_height = 5
    # BUILDING MATERIALS
    air = "air"
    castle = "default:stone"
    window_x = {'name': "xpanes:bar_flat", 'direction': r'(\+|\-)x'}
    window_z = {'name': "xpanes:bar_flat", 'direction': r'(\+|\-)z'}
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
    # BUILD
    b.update(nodebuilder.build(range(castle_x_min - 1, castle_x_min + castle_length + 10), range(floor_y + 1, floor_y + 31), range(player_z - 4, player_z + 5), air))
    b.update(nodebuilder.build(range_x_castle_ext, range_y_castle_ext, range_z_castle_ext, castle))
    b.update(nodebuilder.build(range_x_castle_int, range_y_castle_int, range_z_castle_int, air))
    b.update(nodebuilder.build(castle_x_min, [floor_y + 1, floor_y + 2], player_z, air))
    b.update(nodebuilder.build(range_x_window, range_y_window, (wall_z1, wall_z2), window_z))
    b.update(nodebuilder.build(castle_x_min, floor_y + 4, (player_z - 1, player_z, player_z + 1), window_x))
    return b


class TestCase(GeneralTestCase):
    @mock.patch('ircbuilder.building.Building.send', mock_building_send)
    @mock.patch('ircbuilder.MinetestConnection.create', mock_create)
    def test_building(self):
        from lesson1.task14_castle_windows.task import b
        self.check_building_with_pattern(b, building_pattern)

    def test_by_building_in_minetest(self):
        from lesson1.task14_castle_windows.task import b
        self.check_by_building_in_minetest(b, 14)


if __name__ == '__main__':
    # these steps are not executed when pressing the [Check] button
    configure_logging()
    unittest.main()
