# Task 6 - Placing multiple blocks in one build
There is an even easier way than using `for` loops.

## Task
Place a 3x3x3 cube of glass blocks centred at (100, 14, ref_z). Use wool for the centre block

<img src="glass_cube.png" width="100%" />

## Lesson
Placing multiple blocks of the same kind at the same time is such a common
requirement, the `build` command has been designed to accept number sequences
for the x, y and z coordinates. Previously we have used a `for` loop.

        for y in [13, 14, 15]:
            mc.build(99, y, 0, glass)

This can now be rewritten in one line

        mc.build(99, [13, 14, 15], 0, glass)

It will place three glass blocks at (99, 13, 0), (99, 14, 0) and (99, 15, 0).
Number sequences are not restricted to one parameter. If there is more than one sequence
then it works like nested loops.

        mc.build([99, 100], [13, 14, 15], 0, glass)

places six glass blocks at (99, 13, 0), (99, 14, 0), (99, 15, 0), (100, 13, 0), (100, 14, 0), (100, 15, 0).

Each sequence of numbers can be stored in a variable rather than typed directly
in the `build` command. The numbers in the sequences don't even need to be consecutive.

        seq_x = [99, 101]
        seq_y = [13, 15]
        mc.build(seq_x, seq_y, 0, glass)

places four glass blocks at (99, 13, 0), (99, 15, 0), (101, 13, 0), (101, 15, 0).

## Overwriting positions
If you do more than one `build` command for the same position, the second command will overwrite
the first command.

<br>
<div class='hint'><code>seq_x</code> needs to be a sequnce of values of x for the glass block locations</div>
<div class='hint'><code>seq_x</code> numbers should centre on ref_x</div>
<div class='hint'>Each sequence can use numbers or formulae</div>
<div class='hint'>Enclose values of each sequence in parentheses () or square brackets []</div>
<div class='hint'><code>seq_y</code> needs to be a sequence of y values for the glass blocks</div>
<div class='hint'><code>seq_z</code> needs to be a sequence of z values for the glass blocks</div>

© Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt

