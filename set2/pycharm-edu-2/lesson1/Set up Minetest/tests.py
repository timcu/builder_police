import collections.abc
import json
import logging
import logging.config
import os.path
import re
import subprocess
import sys

from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def test_config():
    # Stepik changes directory structure so check first which directory structure
    config_dir = "../../"
    config_file = "minetest_irc.py"
    if not os.path.exists(f"{config_dir}{config_file}"):
        if os.path.exists(f"../{config_dir}{config_file}"):
            config_dir = f"../{config_dir}"
    config_path = f"{config_dir}{config_file}"
    logging_config_path = f"{config_dir}logging_config.json"
    requirements_path = f"{config_dir}requirements.txt"

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
        from task import logging_config
        logging_config_final = update(logging_config_final, logging_config)
    except ImportError:
        # logging_config not specified so no changes required
        pass
    with open(logging_config_path, "w") as file:
        json.dump(logging_config_final, file)
    logging.config.dictConfig(logging_config_final)

    # Check if ircserver is on LAN
    from task import mtuser, mtuserpass, mtbotnick, ircserver, channel, player_z
    try:
        # check if ircbuilder already installed
        from ircbuilder import open_irc
    except ImportError:
        ircbuilder_version = "0.0.11"  # will get overridden later if requirements.txt set up properly
        with open(requirements_path) as file:
            for line in file:
                print(line)
                if line.startswith("ircbuilder>="):
                    ircbuilder_version = line[len("ircbuilder>="):].strip()
                    break
        if re.fullmatch(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ircserver):
            # install ircbuilder from LAN server
            logging.warning(f"LAN {ircserver}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"http://{ircserver}/download/pypi/ircbuilder/ircbuilder-{ircbuilder_version}.tar.gz"])
        else:
            # install ircbuilder from pypi.org
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"ircbuilder>={ircbuilder_version}"])

    with open(config_path, "w") as file:
        file.write('mtuser = "' + mtuser + '"       # your minetest username\n')
        file.write('mtuserpass = "' + mtuserpass + '"   # your minetest password. This file is not encrypted so don\'t use anything you want kept secret\n')
        file.write('player_z = ' + str(player_z) + '  # your z value from sign in minetest with your username on it\n')
        file.write('\n')
        file.write('# The following must match your settings in minetest server > Settings > Advanced Settings > Mods > irc > Basic >\n')
        file.write('ircserver = "' + ircserver + '"   # same as IRC server\n')
        file.write('mtbotnick = "' + mtbotnick + '"   # same as Bot nickname\n')
        file.write('channel = "' + channel + '"     # same as Channel to join\n')

    from ircbuilder import open_irc
    with open_irc(ircserver, mtuser, mtuserpass, mtbotnick, channel, port=6697) as mc:
        z = mc.send_cmd('get_player_z ' + mtuser)
    try:
        if int(z)!=player_z:
            failed("Your player_z should be " + z + ", not " + str(player_z))
            return False
    except TypeError:
        failed("Didn't get an int for player_z. Instead got " + str(z) + " which has type " + str(type(z)))
        return False
    except ValueError:
        failed("Didn't get an int for player_z. Instead got " + str(z) + " which has type " + str(type(z)))
        return False
    passed()
    return True


if __name__ == '__main__':
    run_common_tests()
    test_config()
    # test_answer_placeholders()       # TODO: uncomment test call


