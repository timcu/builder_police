# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# Authorised for use by CoderDojo in 2018

from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from ircbuilder import MinetestConnection, NICK_MAX_LEN
from coderdojo import ircserver, mtuser, mtuserpass, mtbotnick, channel
import pref

x1 = pref.x-7
x2 = pref.x-30
y = pref.y


def test_nodes():
    placeholders = get_answer_placeholders()
    print("Len of placehoders", len(placeholders))
    for i in range(len(placeholders)):
        print(i, placeholders[i])
    pybotnick = "pt" + mtuser
    if len(pybotnick) > NICK_MAX_LEN:
        pybotnick = pybotnick[0:NICK_MAX_LEN]
    print("about to connect as ",pybotnick, mtuser)
    mc = MinetestConnection.create(ircserver, mtuser, mtuserpass, mtbotnick, channel, pybotnick=pybotnick)
    if placeholders[0] != str(x1):
        failed("You are using incorrect x1 value=" + placeholders[0] + ". Should be " + str(x1))
        return False
    if placeholders[1] != str(x2):
        failed("You are using incorrect x2 value=" + placeholders[1] + ". Should be " + str(x2))
        return False
    if placeholders[2] != str(y):
        failed("You are using incorrect y value=" + placeholders[2] + ". Should be " + str(y))
        return False
    str_z = placeholders[3]
    str_z_correct = mc.send_cmd("get_player_z " + mtuser)
    if str_z_correct != str_z:
        failed("You are using incorrect z value=" + str_z + ". Should be " + str_z_correct)
        return False
    z = int(str_z)
    # roof
    str_count = mc.compare_nodes(x1, y+6, z-2, x2, y+6, z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel roof at y=" + str(y+6) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # left wall
    str_count = mc.compare_nodes(x1, y  , z-2, x2, y+6, z-2, "default:glass")
    if str_count != '0':
        failed("Tunnel wall at z=" + str(z-2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # right wall
    str_count = mc.compare_nodes(x1, y  , z+2, x2, y+6, z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel wall at z=" + str(z+2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # floor
    str_count = mc.compare_nodes(x1, y  , z-2, x2, y  , z+2, "default:glass")
    if str_count != '0':
        failed("Tunnel floor at z=" + str(z+2) + " should be all glass but there are " + str_count + " blocks which are not")
        return False
    # Air
    str_count = mc.compare_nodes(x1, y+1, z-1, x2, y+5, z+1, "air")
    if str_count != '0':
        failed("Tunnel centre should be all air but there are " + str_count + " blocks which are not")
        return False
    passed()
    return True


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":       # TODO: your condition here
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    #test_answer_placeholders()       # TODO: uncomment test call
    test_nodes()


