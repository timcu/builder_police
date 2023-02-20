# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, mock_create, mock_building_send, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    b = {}
    air = "air"
    wall = "default:glass"
    floor = "default:stone"
    torch = "(default:torch|air)"
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
    # range_x_torch = range(x_min, x_min + tunnel_length, 4)
    # BUILD
    b.update(nodebuilder.build(range_x, range_y_ext, range_z_ext, wall))
    b.update(nodebuilder.build(range_x, range_y_int, range_z_int, air))
    b.update(nodebuilder.build(range_x, floor_y, range_z_int, floor))
    b.update(nodebuilder.build(range_x, floor_y + 1, player_z + 1, torch))
    return b


class TestCase(GeneralTestCase):
    @mock.patch('ircbuilder.building.Building.send', mock_building_send)
    @mock.patch('ircbuilder.MinetestConnection.create', mock_create)
    def test_building(self):
        from lesson1.task8_tunnel_floor.task import b
        self.check_building_with_pattern(b, building_pattern)
        torches = 0
        for key, value in b.building.items():
            if value == "default:torch":
                torches += 1
        self.assertEqual(torches, 6, msg=f"You have {torches} torches. Should be 6")

    def test_by_building_in_minetest(self):
        from lesson1.task8_tunnel_floor.task import b
        self.check_by_building_in_minetest(b, 8)


if __name__ == '__main__':
    # these steps are not executed when pressing the [Check] button
    configure_logging()
    unittest.main()
