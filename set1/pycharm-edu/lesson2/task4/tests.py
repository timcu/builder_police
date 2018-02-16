# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_eval, test_string

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_eval(placeholders, 0, "math.floor(x+0.5)", [{'x': -1.49}, {'x': -0.51}, {'x': -0.49}, {'x': 0.49}, {'x': 0.51}, {'x': 1.49}], "math"):
        return False
    if not test_eval(placeholders, 1, "math.floor(y+0.5)", [{'y': -1.49}, {'y': -0.51}, {'y': -0.49}, {'y': 0.49}, {'y': 0.51}, {'y': 1.49}], "math"):
        return False
    if not test_eval(placeholders, 2, "math.floor(z+0.5)", [{'z': -1.49}, {'z': -0.51}, {'z': -0.49}, {'z': 0.49}, {'z': 0.51}, {'z': 1.49}], "math"):
        return False
    if not test_string(placeholders, 3, "15"):
        return False
    if not test_string(placeholders, 4, "20"):
        return False
    if not test_string(placeholders, 5, "10"):
        return False
    if not test_eval(placeholders, 6, '16, 20, 10, "default:glass"', [{}]):
        return False
    if not test_eval(placeholders, 7, '16, 20, z, "default:stone"', [{'z':10}, {'z':11}]):
        return False
    if not test_eval(placeholders, 8, 'x, y, z, "wool:blue"', [{'x':5,'y':25,'z':10}, {'x':55,'y':255,'z':11}]):
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()


