# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_string, test_exec
from html import escape


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    phi = placeholders[0]
    stri = "Answer 1"
    if len(phi) > 50:
        failed(stri + " please keep length to less than 50 characters. Your answer '" + phi + "' is " + str(len(phi)) + " characters.")
        return False
    answer = eval("(" + phi + ")", {}, {})
    print(answer)
    if not isinstance(answer, tuple):
        failed(stri + " is not a tuple. It is a " + escape(str(type(answer))) + ". Your answer '" + phi + "'")
        return False
    print(str(len(answer)))
    if len(answer) != 2:
        failed(stri + " is supposed to contain 2 elements but has " + str(len(answer)) + ". Your answer '" + phi + "'")
        return False
    if not isinstance(answer[0],str):
        failed(stri + " first element is not a string. It is " + repr(answer[0]) + " which has type " + escape(str(type(answer[0]))))
        return False
    print(str(type(answer[1])))
    if not isinstance(answer[1],str):
        failed(stri + " second element is not a string. It is " + repr(answer[1]) + " which has type " + escape(str(type(answer[1]))))
        return False
    phi = placeholders[1]
    stri = "Answer 2"
    if len(phi) > 50:
        failed(stri + " please keep length to less than 50 characters. Your answer '" + phi + "' is " + str(len(phi)) + " characters.")
        return False
    answer = eval("(" + phi + ")", {}, {})
    if not isinstance(answer, tuple):
        failed(stri + " is not a tuple. It is a " + escape(str(type(answer))) + ". Your answer '" + phi + "'")
        return False
    if len(answer) != 3:
        failed(stri + " is supposed to contain 3 elements but has " + str(len(answer)) + ". Your answer '" + phi + "'")
        return False
    if not isinstance(answer[0],str):
        failed(stri + " first element is not a string. It is " + repr(answer[0]) + " which has type " + escape(str(type(answer[0]))))
        return False
    if not isinstance(answer[1],int):
        failed(stri + " second element is not an int. It is " + repr(answer[1]) + " which has type " + escape(str(type(answer[1]))))
        return False
    if not isinstance(answer[2],float):
        failed(stri + " third element is not a float. It is " + repr(answer[2]) + " which has type " + escape(str(type(answer[2]))))
        return False
    if not test_string(placeholders, 2, "1"): return False
    if not test_string(placeholders, 3, "5"): return False
    if not test_exec(placeholders, 4, "x, y, z = t1",[{'t1':(15,6,1234)}]): return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()


