import collections.abc
import json
import logging
import logging.config
import re
import subprocess
import sys
import unittest

from pathlib import Path


def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


class TestCase(unittest.TestCase):

    def test_config(self):
        # Stepik changes directory structure so check first which directory structure
        config_dir = Path("../../")
        config_filename = "minetest_irc.py"
        if not (config_dir / config_filename).exists():
            if (config_dir.parent / config_filename).exists():
                config_dir = config_dir.parent
        config_path = config_dir / config_filename
        logging_config_path = config_dir / "logging_config.json"
        requirements_path = config_dir / "requirements.txt"

        logging_config_final = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                },
            },
            'root': {
                'handlers': ['console'],
                'level': 'WARNING',
            },
        }
        try:
            from lesson1.set_up_minetest.task import logging_config
            logging_config_final = update(logging_config_final, logging_config)
        except ImportError:
            # logging_config not specified so no changes required
            logging_config = None
            logging.debug(f"Import error on logging_config. {logging_config}")
            pass
        with open(logging_config_path, "w") as file:
            json.dump(logging_config_final, file)
        logging.config.dictConfig(logging_config_final)

        # Check if ircserver is on LAN
        from lesson1.set_up_minetest.task import mtuser, mtuserpass, mtbotnick, ircserver, channel, player_z
        try:
            # check if ircbuilder already installed
            from ircbuilder import open_irc
        except ImportError:
            ircbuilder_version = "0.0.12"  # will get overridden later if requirements.txt set up properly
            with open(requirements_path) as file:
                for line in file:
                    print(line)
                    if line.startswith("ircbuilder>="):
                        ircbuilder_version = line[len("ircbuilder>="):].strip()
                        break
            if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ircserver):
                # install ircbuilder from LAN server because students isolated from Internet
                logging.warning(f"LAN {ircserver}")
                url_lan = f"http://{ircserver}/download/pypi/ircbuilder/ircbuilder-{ircbuilder_version}.tar.gz"
                subprocess.check_call([sys.executable, "-m", "pip", "install", url_lan])
            else:
                # install ircbuilder from pypi.org
                subprocess.check_call([sys.executable, "-m", "pip", "install", f"ircbuilder>={ircbuilder_version}"])

        with open(config_path, "w") as file:
            file.write(f'mtuser = "{mtuser}"       # your minetest username\n')
            file.write(f'mtuserpass = "{mtuserpass}"   # your minetest password. This file is not encrypted so '
                       'don\'t use anything you want kept secret\n')
            file.write(f'player_z = {player_z}  # your z value from sign in minetest with your username on it\n')
            file.write('\n')
            file.write('# The following must match your settings in minetest server > Settings > Advanced Settings > '
                       'Mods > irc > Basic >\n')
            file.write('ircserver = "' + ircserver + '"   # same as IRC server\n')
            file.write('mtbotnick = "' + mtbotnick + '"   # same as Bot nickname\n')
            file.write('channel = "' + channel + '"     # same as Channel to join\n')

        from ircbuilder import open_irc
        try:
            with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel, port=6697) as mc:
                z = mc.send_cmd('get_player_z ' + mtuser)
        except Exception as e:
            self.fail(f'Your ircserver setting is bad and raised exception {e}')
        self.assertIsNotNone(z, 'No response. Probably bad mtbotnick or channel')
        self.assertNotEqual(z, 'You are not logged in.', msg=f"Your mtuser or mtuserpass or channel is incorrect")
        self.assertEqual(int(z), player_z, msg=f"Your player_z should be {z}, not {player_z}")
