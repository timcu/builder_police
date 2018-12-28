# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_eval, test_eval_phi, test_exec


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_exec(placeholders, 0, "xmin, y_at_xmin, xmax, y_at_xmax = x2, y2, x1, y1", [
                    {'xmin':1, 'y_at_xmin':2, 'xmax':3, 'y_at_xmax':4, 'x2':50, 'y2':10, 'x1':100, 'y1':15},
                    {'xmin':4, 'y_at_xmin':3, 'xmax':2, 'y_at_xmax':1, 'x2':55, 'y2':12, 'x1':150, 'y1':11}]):
        return False
    if not test_eval(placeholders, 1, "tunnel_y > y_at_xmin", [{'tunnel_y': 50, 'y_at_xmin': 40}, {'tunnel_y': 30, 'y_at_xmin': 35}]):
        return False
    phi = 'dict(' + placeholders[2] + ")"
    if not test_eval_phi(phi, "Answer 3", 'dict(platform_at_xmax, room=room, materials=materials, levels=3)', [
        {'platform_at_xmax':{'x':1, 'levels':1}, 'room':{'length':10}, 'materials':{'stair':'wood'}, 'levels':2},
        {'platform_at_xmax':{'x':3, 'levels':1}, 'room':{'length':15}, 'materials':{'stair':'wool'}, 'levels':1}
    ]):
        return False
    phi = 'dict(' + placeholders[3] + ")"
    if not test_eval_phi(phi, "Answer 4", 'dict(platform_at_xmin, room=room, materials=materials, levels=1)', [
        {'platform_at_xmin':{'x':1, 'levels':1}, 'room':{'length':10}, 'materials':{'stair':'wood'}, 'levels':2},
        {'platform_at_xmin':{'x':3, 'levels':1}, 'room':{'length':15}, 'materials':{'stair':'wool'}, 'levels':1}
    ]):
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()


