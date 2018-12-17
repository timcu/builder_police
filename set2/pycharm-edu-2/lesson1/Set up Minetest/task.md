# Minetest setup

1.  The first step is to play Minetest :). Play online and connect to a Pythonator server.
    You can even connect to the free server at `demo.pythonator.com` using port `30000`.
    Use a name and password of your choosing, and as long as no-one else has chosen that
    name you will be able to login.
2.  Please don't use spaces in your name or password. If you need to change your password in
    Minetest press the [esc] key and click the [Change password] button.
3.  Don't use a password you want keep secret because there is very low security on this
    server and other people can find out your password. I don't mind if your password
    is just "*password*" but be prepared for others to login as you if you
    do that.
4.  Check if you have the `irc_builder` privilege by typing
    `/privs` in Minetest chat. It should be automatic but if not ask
    the Minetest op for that privilege.
5.  Fill in your connection details to Minetest in the program on the left.
    * Enter your name as mtuser (mtuser="myname")
    * Enter your password as mtuserpass (mtuserpass="mysecret")
    * Find your z value from the sign in Minetest with your name in it. Every player gets a unique value.
    * Server details default for the <code>demo.pythonator.com</code> server. For other servers ask your Minetest op.
6.  Click the [Check] button below.
7.  When you have completed this setup correctly you will see "Congratulations!".
    Click the [Next] button to move to the first task.

Here is an example of how to fill in the details for LAN servers at CoderDojo.

    mtuser = "tim"                # your minetest username
    mtuserpass = "not_so_secret"  # your minetest password. This file is not encrypted so don't use anything you want kept secret
    player_z = 10                 # your z value from sign in minetest with your username on it

    # The following must match your settings in minetest server > Settings > Advanced Settings > Mods > irc > Basic >
    ircserver = "192.168.17.100"  # same as IRC server
    mtbotnick = "mtserver"        # same as Bot nickname
    channel = "#coderdojo"        # same as Channel to join

<div class='hint'>
In Minetest, find the sign with your name and your player_z will be the z value on that sign.
</div>
<div class='hint'>Sign will look like the following:<br>
<br>
<div align="center">tim</div>
<div align="center"></div>
<div align="center">x=100</div>
<div align="center">y=14</div>
<div align="center">z=10</div>
<br>
In this case use <code>player_z = 10</code></div>
<div class='hint'>ircserver can be a host name (eg "irc.triptera.com.au") or ip address ("192.168.17.100") of the chat server. </div>
<div class='hint'>Channel names start with ## if it is not a permanent channel, or # for a permanent channel</div>
<br>
