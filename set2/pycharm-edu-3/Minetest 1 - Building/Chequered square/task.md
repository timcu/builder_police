# Task 6 - Chequered square

You should have completed "pythonator b2 easy" course before commencing this course.
In the Minetest world your next task is described on your sign.

## Task

Construct a vertical square shape of alternating wool colours in the sky with height of 9 blocks.
Vertical stripes is an acceptable answer. However, a chequerboard pattern is the complete solution.
All blocks in the square will have the same `z` value.

This course is more advanced than the "pythonator b2 easy" so
you can no longer just type in numbers when the question asks for a variable or formula.

## Lesson

Because the colours are alternating you can't set them all in one `build` command.

The first challenge will be to work out where to start building the square. Try drawing the square
as a grid on a piece of paper and labelling the x and y coordinates of each grid location. The height and width are odd
numbers which is important if you want a single block to be the centre.

We will specify the range of `x` values using `range(x1, x2)`. Therefore `x1` will be the `x` coordinate of one end
of the square and `x2` will be the `x` coordinate one past the opposite end of the square.
Similarly the range of `y` values will be specified using `range(y1, y2)`.
The image below shows the coordinates of the corners of the square in terms of x1, x2, y1 and y2.

Here are the formulae for x1 and x2 in pseudocode. See if you can convert them to Python.

x1 = x at the centre minus (half the width of the square rounded down to nearest integer)
x2 = x1 plus the width of the square

The advantage of using a formula based on centre position and width is that if your requirements change then you
can easily build new squares just by providing a new cx, cy and width/height and not changing any other part of the program.

The second challenge is how to specify a different wool colour each
time a node is set. There are several ways to do this and each one is correct.
One solution can be achieved in one command. Use the hints to see if you can work it out.

<img src="chequered_square.png" width="100%" />

<br>
<div class='hint'>For <code>colour0</code> and <code>colour1</code> choose one of the 16 wool colours
white, grey, dark_grey, black, blue, cyan, green, dark_green, yellow, orange,
brown, red, pink, magenta or violet</div>
<div class='hint'><code>colour1</code> has to be different to <code>colour0</code></div>
<div class='hint'>Width of square is measured in blocks.</div>
<div class='hint'>Height of square is always the same as the width for a square.</div>
<div class='hint'>Calculate <code>x1</code> using a formula based on <code>cx</code> and <code>width</code> which results in the minimum <code>x</code> value for constructing the square</div>
<div class='hint'>x1 should be an <code>int</code>. </div>
<div class='hint'>For x1 use integer division when finding half the width ( width // 2 ) so that result will be an int</div>
<div class='hint'>Calculate <code>y1</code> using a formula based on <code>cy</code> and <code>height</code> which results in the minimum <code>y</code> value for constructing the square</div>
<div class='hint'>
<code>range(stop)               # iterates from 0 to ('stop'-1) counting up in ones</code><br />
<code>range(start, stop)        # iterates from 'start' to ('stop'-1) counting up in ones</code><br />
<code>range(start, stop, step)  # iterates from 'start' to but not including 'stop' counting in 'step's</code><br />
</code></div>
<div class='hint'>When setting <code>colour</code>, adjacent blocks (x differs by one) with the same value of y must have different colours</div>
<div class='hint'><div>colours[0] will use one colour</div>
<div>colours[1] will use the other colour</div></div>
<div class='hint'><p>Statement setting <code>colour</code> will look like</p>
<p>colour = colours['formula']</p>
<p>But you need to replace 'formula' with a formula or variable which returns a 0 or 1 depending in which colour you want </p></div>
<div class='hint'>Choose different colours using modulo arithmetic</div>
<div class='hint'><p>The modulo operator is %. It gives the remainder after dividing. </p>
<pre><code>5 % 2 = 1
6 % 2 = 0
7 % 2 = 1</code></pre>
</div>
<div class='hint'><p>Using modulo operator in a <code>for</code> loop. </p>
<pre><code>x % 2 = 1  # when x == 5
x % 2 = 0  # when x == 6
x % 2 = 1  # when x == 7</code></pre>
</div>
<div class='hint'><p>Using modulo operator in a <code>for</code> loop with two variables. </p>
<pre><code>(x + y) % 2 = 1  # when x == 5 and y == 4
(x + y) % 2 = 0  # when x == 6 and y == 4
(x + y) % 2 = 1  # when x == 7 and y == 4
</code></pre>
</div>

<br>
