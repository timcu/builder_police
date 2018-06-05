# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_eval, test_exec

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_eval(placeholders, 0, "platform['z']", [{'platform':{'z':10}},{'platform':{'z':20}}]):
        return False
    if not test_eval(placeholders, 1, "room['height'] if 'height' in room else 5", [{'room':{'height':6}},{'room':{'height':1}},{'room':{'length':20}}]):
        return False
    if not test_eval(placeholders, 2, "materials['station_stair'] if 'station_stair' in materials else 'stairs:stair_wood'", [{'materials':{'station_stair':'stairs:stair_stonebrick'}},{'materials':{'station_stair':'stairs:stair_stone'}},{'materials':{'length':20}}]):
        return False
    if not test_eval(placeholders, 3, "door[:-2]", [{'door':'doors:door_wood_a'},{'door':'doors:door_wood_b'},{'door':'doors:door_iron_a'}]):
        return False
    if not test_eval(placeholders, 4, "range(levels)", [{'levels':3},{'levels':5}]):
        return False
    if not test_eval(placeholders, 5, "station_width + 2 - 2 * roof_layer", [{'station_width':10, 'roof_layer':1},{'station_width':9, 'roof_layer':3}]):
        return False
    passed()


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()


