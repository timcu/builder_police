# Task 1a - Placing a block
Let's start building!

## Task
Visit the Minetest world and find your sign. It will have coordinates where you need to
create a wool block. Enter the z coordinate in the program on the left.

<img src="wool_green.png" width="100%" />

## Lesson
This first task teaches you how to place a block using the `build` command from `MinetestConnection`.
The following line places a stone block at x=100, y=14, z=0. The `build` command saves all the blocks
in a `building` and then the `building` is sent to Minetest using the `send_building` command.

        mc.build(100, 14, 0, "default:stone")
        mc.send_building()

The `build` command has 4 parameters.
They are x, y, z, and node_type. The first 3 parameters are the coordinates where the node will be placed.
The last parameter is the name of the material to place. Examples are "default:wood", "default:dirt", "wool:blue", "default:glass", "carts:rail".
The material names are the name of the mod they come from, a colon (:), and then the material name within that mod.

Hints are available by clicking the light bulbs below.

Click the [Check] button below to check you have completed the task correctly.
Checking the task does not run the task so it will not build anything in the Minetest world.

Click the green triangle "play" button to run your program or use keyboard ctrl-shift-F10.
This will build your construction in the Minetest world. It is safer to wait until your task checks completely before
building it in Minetest world. However, sometimes it is hard to see where the problem is, so try running it with
the green triangle or ctrl-shift-F10 to build your structure in Minetest. Then play Minetest
and examine what you have built to see where the problem is with your code.

When you have completed this task (Congratulations!) click the [Next] button to
move to the next task.

<div class='hint'>The sign asks for orange wool but any colour will be considered correct.</div>
<div class='hint'>The missing number is the z coordinate where you want to place the wool.</div>
<div class='hint'>Find the z coordinate by logging in to Minetest and finding the sign with your name on it.</div>

