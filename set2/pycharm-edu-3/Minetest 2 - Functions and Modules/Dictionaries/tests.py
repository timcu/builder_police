# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by schools and CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from triptera_pe_tests import test_eval, test_exec


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if not test_eval(placeholders, 0, "dict()", list_data=[{}]): return False
    if not test_exec(placeholders, 1, "scores['andy']=10",[{"scores":{}}]): return False
    if not test_exec(placeholders, 2, "scores['betty']=15",[{"scores":{'andy':10}}]): return False
    if not test_exec(placeholders, 3, "scores['cathy']=12",[{"scores":{'andy':10, 'betty':15}}]): return False
    if not test_exec(placeholders, 4, "scores['andy']=scores['andy']+3",[{"scores":{'andy':10, 'betty':15, 'cathy':12}}]): return False
    if not test_eval(placeholders, 5, "scores.items()", list_data=[{"scores":{'andy':13, 'betty':15, 'cathy':12}}]): return False
    if not test_eval(placeholders, 6, "score", list_data=[{"score":13}, {'score':15}, {'score':12}]): return False
    if not test_eval(placeholders, 7, "score", list_data=[{"score":13}, {'score':15}, {'score':12}]): return False
    if not test_eval(placeholders, 8, "name", list_data=[{"name":'andy'}, {'name':'betty'}, {'name':'cathy'}]): return False
    passed()
    return True


if __name__ == '__main__':
    if test_answer_placeholders():
        run_common_tests()
