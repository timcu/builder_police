# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
#from ircbuilder import MinetestConnection, NICK_MAX_LEN
#from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
from triptera_pe_tests import test_eval, test_minetest

def test_answer_placeholders():
    x1 = 69
    y1 = 14
    x2 = 9
    y2 = -46
    placeholders = get_answer_placeholders()
    if not test_eval(placeholders, 0, 'x1-x2+1', [{'x1':69, 'x2':9}, {'x1':70, 'x2':35}]): return False
    if not test_eval(placeholders, 1, 'x1-i', [{'x1':69, 'i':0}, {'x1': 70, 'i':35}]): return False
    if not test_eval(placeholders, 2, 'y1-i', [{'y1':14, 'i':0}, {'y1':-46, 'i':15}]): return False

    ph=placeholders[3]
    if len(ph)>10:
        return failed("torch condition should be less than 10 characters long. It is '" + ph + "' which has length " + str(len(ph)))
    count=0
    try:
        for i in range(x1-x2+1):
            x = x1-i
            y = y1-i
            if eval(ph, {'i':i, 'x':x, 'y':y}):
                count += 1
        if count >= 61 / 3 or count <= 61 / 5:
            failed("torch condition returned True " + str(count) + " times but it should be between 12 and 20 times")
            return False
    except NameError:
        failed("torch condition should only be based on i or x or y. Instead it is " + ph)
        return False
    passed()


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()
        test_minetest(8)

