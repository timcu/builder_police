# © Copyright 2018-2023 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use in schools and CoderDojo sessions in 2018 - 2019

import importlib
import json
import logging.config
import os
import re
import time
import unittest

from copy import deepcopy

from ircbuilder import MinetestConnection, NICK_MAX_LEN, open_irc
from lesson1.set_up_minetest.task import player_z


class GeneralTestCase(unittest.TestCase):
    def check_minetest(self, num_task):
        from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel
        pybotnick = "pt" + mtuser
        if len(pybotnick) > NICK_MAX_LEN:
            pybotnick = pybotnick[0:NICK_MAX_LEN]
        with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick) as mc:
            task = int(mc.send_cmd("get_player_task " + mtuser))
        self.assertTrue(task > num_task,
                        msg=f"Check 'Task {num_task} Assessment' sign in minetest to find out what else is required")

    def check_by_building_in_minetest(self, b, num_task):
        from lesson1.set_up_minetest.task import ircserver, mtuser, mtuserpass, mtbotnick, channel
        pybotnick = "pt" + mtuser
        if len(pybotnick) > NICK_MAX_LEN:
            pybotnick = pybotnick[0:NICK_MAX_LEN]
        with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick) as mc:
            b.send(mc)
            time.sleep(1)
            task = int(mc.send_cmd("get_player_task " + mtuser))
            if task <= num_task:
                # Give minetest time to build and assess
                logging.info("Waiting for minetest to assess your building")
                time.sleep(10)
                task = int(mc.send_cmd("get_player_task " + mtuser))
        self.assertTrue(task > num_task,
                        msg=f"Check 'Task {num_task} Assessment' sign in minetest to find out what else is required")

def test_eval_phi(phi, str_answer_number, answer, list_data, modules=()):
    if len(phi) > len(answer) + 5:
        failed(str_answer_number + " is too long. Correct answer only " + str(len(answer)) + " characters long. Your answer " + phi + " has length " + str(len(phi)))
        return False
    if not list_data:
        list_data = [{}]
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

    def check_eval(self, placeholders, i, answer, list_data=None, modules=()):
        str_answer_number = "Answer " + str(i+1)
        return self.check_eval_phi(placeholders[i], str_answer_number, answer, list_data, modules)

    def check_string(self, placeholders, i, answer):
        phi = placeholders[i]
        stri = "Answer " + str(i+1)
        self.assertEqual(phi, answer, msg=f"{stri} should be {answer}. You entered {phi}")

    def check_string_in(self, placeholders, i, list_answer):
        phi = placeholders[i]
        stri = "Answer " + str(i+1)
        self.assertIn(phi, list_answer, msg=f"{stri} should be one of {list_answer}. You entered {phi}")

    def check_exec(self, placeholders, i, answer, list_data, modules=()):
        phi = placeholders[i]
        stri = "Answer " + str(i+1)
        # print("test_assignment",stri,phi, list_data)
        self.assertLessEqual(len(phi), len(answer) + 5,
                             msg=f"{stri} is too long. Correct answer only {len(answer)} characters long. "
                                 f"Your answer {phi} has length {len(phi)}")
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
                self.fail(f"{stri} should only be in terms of variables {list_vars} but includes other "
                          f"variables. It is {phi}")
            exec(answer, global_data, locals_answer)
            # print("answer", locals_answer, "guess", locals_guess)
            for k, v in locals_answer.items():
                # print("k",k,"v",v,"guess[k]",locals_guess[k])
                if v != locals_guess[k]:
                    self.fail(f"{stri} gave incorrect answer for data {data}. Correct answer: {locals_answer}. Your "
                              f"answer: {locals_guess}. Your statement: {phi}")

    def check_building_with_pattern(self, building, building_pattern):
        building_guess = building.building
        building_correct = building_pattern(player_z)
        for key, pattern in building_correct.items():
            try:
                guess = building_guess[key]
            except KeyError:
                self.fail(f"Missing build at {key}. Should match {pattern}")
            if guess[0] == '{':
                guess_dict = json.loads(guess)
            else:
                guess_dict = {'name': guess}
            if pattern[0] == '{':
                pattern = json.loads(pattern)
            try:
                guess_dict['name']
            except KeyError:
                self.fail(f"Dict missing 'name' at {key}. Dict is {guess_dict} which should match {pattern}")
            self.assertIsInstance(guess_dict['name'], str,
                                  msg=f"Dict 'name' not str at {key}. Dict is {guess_dict} of which 'name' is type "
                                      f"{type(guess_dict['name'])} but should be a str matching {pattern}")
            if isinstance(pattern, str):
                if not re.fullmatch(pattern, guess_dict['name']):
                    self.fail(f"Build at {key} is {guess_dict['name']} which doesn't match {pattern}")
            else:
                for pat_key, pat_pattern in pattern.items():
                    if pat_key == 'name':
                        if not re.fullmatch(pat_pattern, guess_dict['name']):
                            self.fail(f"Build 'name' at {key} is {guess_dict['name']} and doesn't match {pat_pattern}")
                    else:
                        try:
                            guess_dict[pat_key]
                        except KeyError:
                            self.fail(f"Guess at {key} is {guess} missing '{pat_key}' which should match {pat_pattern}")
                        if not re.fullmatch(pat_pattern, guess_dict[pat_key]):
                            self.fail(f"Guess at {key} is {guess} wrong '{pat_key}' which should match {pat_pattern}")


def mock_send_building(end_list=()):
    pass


def mock_create(ircserver, mtuser, mtuserpass, mtbotnick="mtserver", channel=None, pybotnick=None, port=6697):
    if not pybotnick:
        pybotnick = "py" + mtuser
    mc = MinetestConnection(ircserver, mtbotnick, pybotnick, port)
    # mc.send_string("USER " + pybotnick + " 0 * :" + pybotnick)
    # user authentication  first pybotnick is username, second pybotnick is real name
    # mc.send_string("NICK " + pybotnick) # assign the nick to this python app
    # mc.wait_for_message_num(376) # End of MOTD
    # mc.join_channel(channel)
    # mc.wait_for_message_num(366) # End of NAMES list
    # mc.send_irccmd("login " + mtuser + " " + mtuserpass)
    return mc


def mock_send_node_lists(mc, node_lists, end_list=()):
    return


def mock_building_send(mc, end_list=()):
    return


def configure_logging():
    # Stepik changes directory structure so check first which directory structure
    config_dir = "../../"
    config_file = "logging_config.json"
    if not os.path.exists(f"{config_dir}{config_file}"):
        if os.path.exists(f"../{config_dir}{config_file}"):
            config_dir = f"../{config_dir}"
    logging_config_path = f"{config_dir}{config_file}"
    with open(logging_config_path, "r") as file:
        logging.config.dictConfig(json.load(file))
