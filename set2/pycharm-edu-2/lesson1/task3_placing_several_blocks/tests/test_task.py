# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, mock_create, mock_building_send, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    ref_z = player_z
    wool = r"wool:(white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet)"
    glass = r"default:glass"

    b = {}
    b.update(nodebuilder.build(100, 13, ref_z - 1, glass))
    b.update(nodebuilder.build(100, 14, ref_z - 1, glass))
    b.update(nodebuilder.build(100, 15, ref_z - 1, glass))
    b.update(nodebuilder.build(100, 13, ref_z, glass))
    b.update(nodebuilder.build(100, 14, ref_z, wool))
    b.update(nodebuilder.build(100, 15, ref_z, glass))
    b.update(nodebuilder.build(100, 13, ref_z + 1, glass))
    b.update(nodebuilder.build(100, 14, ref_z + 1, glass))
    b.update(nodebuilder.build(100, 15, ref_z + 1, glass))
    return b


class TestCase(GeneralTestCase):
    @mock.patch('ircbuilder.building.Building.send', mock_building_send)
    @mock.patch('ircbuilder.MinetestConnection.create', mock_create)
    def test_building(self):
        from lesson1.task3_placing_several_blocks.task import b
        return self.check_building_with_pattern(b, building_pattern)

    def test_by_building_in_minetest(self):
        from lesson1.task3_placing_several_blocks.task import b
        self.check_by_building_in_minetest(b, 3)


if __name__ == '__main__':
    # these steps are not executed when pressing the [Check] button
    configure_logging()
    unittest.main()
