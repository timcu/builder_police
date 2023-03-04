import collections.abc
import json
import logging
import logging.config
import re
import subprocess
import sys
import unittest

from pathlib import Path


class TestCase(unittest.TestCase):

    def test_config(self):
        # Stepik changes directory structure so check first which directory structure
        reqs_dir = Path("../../")
        reqs_filename = "requirements.txt"
        if not (reqs_dir / reqs_filename).exists():
            if (reqs_dir.parent / reqs_filename).exists():
                reqs_dir = reqs_dir.parent
        requirements_path = reqs_dir / reqs_filename

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

        from ircbuilder import open_irc
        try:
            with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel, port=6697) as mc:
                z = mc.send_cmd('get_player_z ' + mtuser)
        except Exception as e:
            self.fail(f'Your ircserver setting is bad and raised exception {e}')
        self.assertIsNotNone(z, 'No response. Probably bad mtbotnick or channel')
        self.assertNotEqual(z, 'You are not logged in.', msg=f"Your mtuser or mtuserpass or channel is incorrect")
        self.assertEqual(int(z), player_z, msg=f"Your player_z should be {z}, not {player_z}")
