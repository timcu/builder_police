# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import failed, passed
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from minetest_irc import ircserver, mtuser, mtuserpass, mtbotnick, channel, player_z
from copy import deepcopy
import importlib
import json
import re

def test_minetest(num_task):
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    task = int(mc.send_cmd("get_player_task " + mtuser))
    if task > num_task:
        passed()
        return True
    else:
        failed("Failed: Check 'Task " + str(num_task) + " Assessment' sign in minetest to find out what else is required")
        return False


def test_eval_phi(phi, str_answer_number, answer, list_data, modules=()):
    if len(phi) > len(answer) + 5:
        failed(str_answer_number + " is too long. Correct answer only " + str(len(answer)) + " characters long. Your answer " + phi + " has length " + str(len(phi)))
        return False
    global_data = {}
    if isinstance(modules, str):
        modules = (modules,)
    for module in modules:
        global_data[module] = importlib.import_module(module)
    for data in list_data:
        try:
            guess = eval(phi, global_data, data)
        except NameError:
            list_vars = ""
            comma = ""
            for k in data:
                list_vars += comma + k
                comma = ", "
            failed(str_answer_number + " should only be in terms of variables " + list_vars + " but includes other variables. It is " + phi)
            return False
        except KeyError:
            failed(str_answer_number + " had a KeyError. Your answer " + phi)
            return False
        correct = eval(answer, global_data, data)
        if guess != correct:
            failed(str_answer_number + " gave incorrect answer for data " + str(data) + ". Correct answer: " + str(correct) + ". Your answer: " + str(guess) + ". Your formula: " + phi)
            return False
    return True


def test_eval(placeholders, i, answer, list_data, modules=()):
    str_answer_number = "Answer " + str(i+1)
    return test_eval_phi(placeholders[i], str_answer_number, answer, list_data, modules)


def test_string(placeholders, i, answer):
    phi = placeholders[i]
    stri = "Answer " + str(i+1)
    if phi != answer:
        failed(stri + " should be " + answer + ". You entered " + phi)
        return False
    return True


def test_string_in(placeholders, i, list_answer):
    phi = placeholders[i]
    stri = "Answer " + str(i+1)
    if phi not in list_answer:
        failed(stri + " should be one of " + str(list_answer) + ". You entered " + phi)
        return False
    return True


def test_exec(placeholders, i, answer, list_data, modules=()):
    phi = placeholders[i]
    stri = "Answer " + str(i+1)
    # print("test_assignment",stri,phi, list_data)
    if len(phi) > len(answer) + 5:
        failed(stri + " is too long. Correct answer only " + str(len(answer)) + " characters long. Your answer " + phi + " has length " + str(len(phi)))
        return False
    global_data = {}
    if isinstance(modules, str):
        modules = (modules,)
    for module in modules:
        global_data[module] = importlib.import_module(module)
    for data in list_data:
        locals_guess = deepcopy(data)
        locals_answer = deepcopy(data)
        try:
            exec(phi, global_data, locals_guess)
        except NameError:
            list_vars = ""
            comma = ""
            for k in data:
                list_vars += comma + k
                comma = ", "
            failed(stri + " should only be in terms of variables " + list_vars + " but includes other variables. It is " + phi )
        exec(answer, global_data, locals_answer)
        # print("answer", locals_answer, "guess", locals_guess)
        for k,v in locals_answer.items():
            # print("k",k,"v",v,"guess[k]",locals_guess[k])
            if v != locals_guess[k]:
                failed(stri + " gave incorrect answer for data " + str(data) + ". Correct answer: " + str(locals_answer) + ". Your answer: " + str(locals_guess) + ". Your statement: " + phi)
                return False
    return True


def test_building_with_pattern(mc, building_pattern):
    #player_z = int(mc.send_cmd('get_player_z ' + mtuser))
    building_guess = mc.building
    building_correct = building_pattern(player_z)
    for key, pattern in building_correct.items():
        try:
            guess = building_guess[key]
        except KeyError:
            failed("Missing build at " + str(key) + ". Should match " + str(pattern) )
            return False
        if guess[0]=='{':
            guess_dict=json.loads(guess)
        else:
            guess_dict = {'name': guess}
        if pattern[0]=='{':
            pattern=json.loads(pattern)
        try:
            guess_dict['name']
        except KeyError:
            failed("Dict missing 'name' at " + str(key) + ". Dict is " + str(guess_dict) + " which should match " + str(pattern) )
            return False
        if not isinstance(guess_dict['name'], str):
            failed("Dict 'name' not str at " + str(key) + ". Dict is " + str(guess_dict) + " of which 'name' is type " + str(type(guess_dict['name'])) + " but should be a str matching " + str(pattern) )
            return False
        if isinstance(pattern, str):
            if not re.fullmatch(pattern, guess_dict['name']):
                failed("Build at " + str(key) + " is " + guess_dict['name'] + " which doesn't match " + pattern)
                return False
        else:
            for pat_key, pat_pattern in pattern.items():
                if pat_key == 'name':
                    if not re.fullmatch(pat_pattern, guess_dict['name']):
                        failed("Build 'name' at " + str(key) + " is " + guess_dict['name'] + " which doesn't match " + pat_pattern)
                        return False
                else:
                    try:
                        guess_dict[pat_key]
                    except KeyError:
                        failed("Guess at " + str(key) + " is " + str(guess) + " missing '" + pat_key + "' which should match " + pat_pattern)
                        return False
                    if not re.fullmatch(pat_pattern, guess_dict[pat_key]):
                        failed("Guess at " + str(key) + " is " + str(guess) + " wrong '" + pat_key + "' which should match " + pat_pattern)
                        return False
    passed()
    return True


def mock_send_building(self, end_list=()):
    pass


@staticmethod
def mock_create(ircserver, mtuser, mtuserpass, mtbotnick = "mtserver", channel = None, pybotnick = None, port = 6667 ):
    if not pybotnick:
        pybotnick = "py" + mtuser
    mc = MinetestConnection(ircserver,mtbotnick,pybotnick,port)
    # mc.send_string("USER " + pybotnick + " 0 * :" + pybotnick) # user authentication  first pybotnick is username, second pybotnick is real name
    # mc.send_string("NICK " + pybotnick) # assign the nick to this python app
    # mc.wait_for_message_num(376) # End of MOTD
    # mc.join_channel(channel)
    # mc.wait_for_message_num(366) # End of NAMES list
    # mc.send_irccmd("login " + mtuser + " " + mtuserpass)
    return mc


