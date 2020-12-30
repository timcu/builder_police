# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_create, mock_building_send
from unittest import mock
from ircbuilder import nodebuilder


def building_pattern(player_z):
    return nodebuilder.build(100, 14, player_z, r"wool:(white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet)")


def test_building():
    from task import b
    # print(f"{b.building=}")
    return test_building_with_pattern(b, building_pattern)


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


@mock.patch('ircbuilder.building.Building.send', mock_building_send)
@mock.patch('ircbuilder.MinetestConnection.create', mock_create)
def run_patched_tests():
    run_common_tests()
    # test_answer_placeholders()       # TODO: uncomment test call
    test_building()


if __name__ == '__main__':
    run_patched_tests()
