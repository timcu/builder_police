# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_building_send, mock_create, configure_logging
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    ref_z = player_z

    b = {}
    glass = "default:obsidian_glass"

    b.update(nodebuilder.build(101, (13, 14, 15), (ref_z - 1, ref_z, ref_z + 1), glass))
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
    configure_logging()
    run_patched_tests()
