# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, mock_create, mock_building_send, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    # BUILDING MATERIALS
    air = "air"
    wall = "default:glass"
    floor = "default:stone"
    torch = "default:torch"
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
    range_y_int = range(floor_y + 1, floor_y + arch_height - 1)
    range_z_int = range(wall_z + 1, wall_z + arch_width - 1)
    # BUILD
    b.update(nodebuilder.build(range(path_x_min, path_x_min + 40), range(floor_y + 1, floor_y + 31), range(player_z - 4, player_z + 5), air))
    b.update(nodebuilder.build(range_x_arch, range_y_ext, range_z_ext, wall))
    b.update(nodebuilder.build(range_x_arch, range_y_int, range_z_int, air))
    b.update(nodebuilder.build(range_x_arch, floor_y, range_z_int, floor))
    b.update(nodebuilder.build(range_x_arch, floor_y + 1, player_z + 1, torch))
    return b


class TestCase(GeneralTestCase):
    @mock.patch('ircbuilder.building.Building.send', mock_building_send)
    @mock.patch('ircbuilder.MinetestConnection.create', mock_create)
    def test_building(self):
        from lesson1.task11_arch_floor.task import b
        self.check_building_with_pattern(b, building_pattern)

    def test_by_building_in_minetest(self):
        from lesson1.task11_arch_floor.task import b
        self.check_by_building_in_minetest(b, 11)


if __name__ == '__main__':
    # these steps are not executed when pressing the [Check] button
    configure_logging()
    unittest.main()
