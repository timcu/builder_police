# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_eval, test_exec


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_exec(placeholders, 0, "from minetest_helper import set_node", []):
        return False
    if not test_eval(placeholders, 1, "1 if x2 > x1 else -1", [{'x1': 1, 'x2': 5}, {'x1':10, 'x2':9}]):
        return False
    if not test_eval(placeholders, 2, "1 if y2 > y1 else -1", [{'y1': 1, 'y2': 5}, {'y1':10, 'y2':9}]):
        return False
    if not test_eval(placeholders, 3, "1 if z2 > z1 else -1", [{'z1': 1, 'z2': 5}, {'z1':10, 'z2':9}]):
        return False
    if not test_exec(placeholders, 4, "node_lists[item] = []", [{'node_lists': {}, 'item': "air"}, {'node_lists': {'air': [(1,2,3)]}, 'item':"default:stone"}]):
        return False
    if not test_exec(placeholders, 5, "node_lists[item].append(pos)", [{'node_lists': {'air':[]}, 'item': "air", "pos": (10, 20, 30)}, {'node_lists': {'air': [(1,2,3)]}, 'item':"air", 'pos':(2,3,4)}]):
        return False
    if not test_exec(placeholders, 6, "item_list.append(key)", [{'item_list': ['air'], 'key': "default:stone"}, {'item_list': ['default:glass'], 'key': "default:wood"}]):
        return False
    if not test_eval(placeholders, 7, "node_lists[item]", [{'node_lists': {'air':[(10, 20, 30)]}, 'item': "air" }, {'node_lists': {'air': [(1,2,3),(2,3,4)]}, 'item':"air"}]):
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()

