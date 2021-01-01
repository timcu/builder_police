# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_building_send, mock_create, configure_logging
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


def test_building():
    from task import b
    if test_building_with_pattern(b, building_pattern):
        torches = 0
        for key, value in b.building.items():
            if value == "default:torch":
                torches += 1
        if torches < 5:
            failed("Only " + str(torches) + " torches. Should be 6")
            return False
        if torches > 6:
            failed("Too many torches. Should be 6. There are " + str(torches))
            return False
        return True
    else:
        return False


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
    configure_logging()
    run_patched_tests()
