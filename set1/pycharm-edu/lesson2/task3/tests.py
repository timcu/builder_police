# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, passed, get_answer_placeholders
from triptera_pe_tests import test_exec, test_string, test_eval
import math

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_string(placeholders, 0, "15"):
        return False
    if not test_string(placeholders, 1, "20"):
        return False
    if not test_string(placeholders, 2, "10"):
        return False
    if not test_exec(placeholders, 3, "node_dict[(16, 20, 10)] = 'default:glass'", [{'node_dict': {(15, 20, 10): 'default:wood'}}]):
        return False
    if not test_exec(placeholders, 4, "node_dict[(16, 20, z)] = 'default:stone'", [
            {'z': 10, 'node_dict': {(15, 20, 10): 'default:wood', (16, 20, 10): 'default:glass'}},
            {'z': 11, 'node_dict': {(15, 20, 10): 'default:wood', (16, 20, 10): 'default:glass'}}]):
        return False
    if not test_exec(placeholders, 5, "del(node_dict[(x, y, z)])", [{'x': 15, 'y': 20, 'z': 10.1, 'node_dict': {(15, 20, 10.1): 'wool:blue'}}]):
        return False
    if not test_eval(placeholders, 6, "math.floor(z+0.5)", [{'z': -1.49}, {'z': -0.51}, {'z': -0.49}, {'z': 0.49}, {'z': 0.51}, {'z': 1.49}], modules="math"):
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()
