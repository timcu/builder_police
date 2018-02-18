# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, get_answer_placeholders, passed, failed
from triptera_pe_tests import test_minetest, test_eval, test_string
import json


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    s = placeholders[0]
    if not s or len(s) < 4:
        failed("Answer 1 missing. You have " + str(s))
        return False
    if s[1] != "{" or s[-2] != "}":
        failed("Answer 1 required a JSON string (starts with '{' and ends with '}'. You have " + str(s))
        return False
    try:
        j = json.loads(s[1:-1])
    except:
        failed("Answer 1 exception when converting from JSON. You have " + str(s))
        return False
    if "param2" not in j:
        failed("Answer 1 requires a param2 attribute. You have " + str(s))
        return False
    if str(j["param2"]) != "1":
        failed("Answer 1 has wrong value of param2. Needs to be for upward in increasing x direction. You have " + str(s))
        return False
    if not test_eval(placeholders, 1, "'carts:rail'", [{}]):
        return False
    if not test_eval(placeholders, 2, "'carts:powerrail'", [{}]):
        return False
    if not test_eval(placeholders, 3, "x//2%2", [{'x':0},{'x':1},{'x':2},{'x':3},{'x':4}]):
        return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()
        test_minetest(9)

