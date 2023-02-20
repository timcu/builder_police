# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, mock_create, mock_building_send, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    return nodebuilder.build(100, 14, player_z, r"wool:(white|grey|dark_grey|black|blue|cyan|green|dark_green|"
                                                r"yellow|orange|brown|red|pink|magenta|violet)")


class TestCase(GeneralTestCase):
    @mock.patch('ircbuilder.building.Building.send', mock_building_send)
    @mock.patch('ircbuilder.MinetestConnection.create', mock_create)
    def test_building(self):
        from lesson1.task1_placing_a_block.task import b
        return self.check_building_with_pattern(b, building_pattern)

    def test_by_building_in_minetest(self):
        from lesson1.task1_placing_a_block.task import b
        self.check_by_building_in_minetest(b, 1)


if __name__ == '__main__':
    # these steps are not executed when pressing [Check] button
    configure_logging()
    unittest.main()
