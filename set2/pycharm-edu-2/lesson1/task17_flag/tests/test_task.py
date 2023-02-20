# © Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com
import unittest

from triptera_pe_tests import GeneralTestCase, configure_logging

class TestCase(GeneralTestCase):
    def test_by_building_in_minetest(self):
        from lesson1.task17_flag.task import b
        self.check_by_building_in_minetest(b, 17)


if __name__ == '__main__':
    # these steps are not executed when pressing the [Check] button
    configure_logging()
    unittest.main()
