# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018 - 2019

from test_helper import run_common_tests, get_answer_placeholders
from triptera_pe_tests import test_building_with_pattern, mock_send_building, mock_create, test_eval, passed
from unittest import mock
from ircbuilder import nodebuilder


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    # Answer 0 can be str or dict. If str then convert to dict before testing
    s = eval(placeholders[0])
    if isinstance(s, str):
        placeholders[0] = s
    s = eval(placeholders[0])
    if "direction" in s:
        if not test_eval(placeholders, 0, '{"name": "stairs:stair_stonebrick", "direction": "+x"}', [{}]):
            return False
    else:
        if not test_eval(placeholders, 0, '{"name": "stairs:stair_stonebrick", "param2": "1"}'):
            return False
    if not test_eval(placeholders, 1, "'carts:rail'", [{}]):
        return False
    if not test_eval(placeholders, 2, "'carts:powerrail'", [{}]):
        return False
    if not test_eval(placeholders, 3, "x//2%2", [{'x': 0}, {'x': 1}, {'x': 2}, {'x': 3}, {'x': 4}]):
        return False
    passed()
    return True


def building_pattern(player_z):
    b = {}
    # start point of tunnel
    x1 = 69
    x2 = 9
    task4_x1 = 93
    y1 = 14
    z = player_z
    num_segments = x1 - x2 + 1

    # store node types in variables for easier use
    ph = get_answer_placeholders()[0]
    if "param2" in ph:
        stair_up_x = {"name": "stairs:stair_stonebrick", "param2": "1"}
    else:
        stair_up_x = {"name": "stairs:stair_stonebrick", "direction": "+x"}
    rail = 'carts:rail'
    power_rail = 'carts:powerrail'

    # sloping section of tunnel
    for i in range(num_segments):
        # Add stairs - Don't need stairs on very last block. Hence check i < 60
        if i < 60:
            b.update(nodebuilder.build(x1 - i, y1 - i, z - 1, stair_up_x))
        # Add power rail
        b.update(nodebuilder.build(x1 - i, y1 - i + 1, z, power_rail))

    # flat section of tunnel
    for x in range(x1, task4_x1 + 1):
        # Add rail or power rail in pairs
        if x // 2 % 2 == 0:
            b.update(nodebuilder.build(x, y1 + 1, z, rail))
        else:
            b.update(nodebuilder.build(x, y1 + 1, z, power_rail))
    return b


def test_building():
    from task import mc
    return test_building_with_pattern(mc, building_pattern)


@mock.patch('ircbuilder.MinetestConnection.create', mock_create)
@mock.patch('ircbuilder.MinetestConnection.send_building', mock_send_building)
def run_patched_tests():
    run_common_tests()
    test_building()


if __name__ == '__main__':
    if test_answer_placeholders():
        run_patched_tests()
