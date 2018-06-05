from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


def test_config():
    from task import mtuser, mtuserpass, mtbotnick, ircserver, channel, player_z
    file = open("../../minetest_irc.py", "w")
    file.write('mtuser = "' + mtuser + '"       # your minetest username\n')
    file.write('mtuserpass = "' + mtuserpass + '"   # your minetest password. This file is not encrypted so don\'t use anything you want kept secret\n')
    file.write('player_z = ' + str(player_z) + '  # your z value from sign in minetest with your username on it\n')
    file.write('\n')
    file.write('# The following must match your settings in minetest server > Settings > Advanced Settings > Mods > irc > Basic >\n')
    file.write('ircserver = "' + ircserver + '"   # same as IRC server\n')
    file.write('mtbotnick = "' + mtbotnick + '"   # same as Bot nickname\n')
    file.write('channel = "' + channel + '"     # same as Channel to join\n')
    file.close()
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel)
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


