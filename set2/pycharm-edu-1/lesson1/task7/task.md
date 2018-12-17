## Lesson
To make a game different every time you play,
you can use a random number generator to emulate the roll of a die. The `random` module has
a `randint(a,b)` function which will return a random integer between the values of `a` and
`b` inclusive. You will often use this function when writing games.

## Program
Returns a random value between 1 and 6 every time the program is run. This simulates the roll
of a six-sided die.

## Task
Write the program to just return a random number between 1 and 6. The program can be three lines long.

The first line needs to import the correct function from the random module. Remember in the previous task
the sleep function was imported from the time module using:

        from time import sleep

The second line needs to call the imported function and store the result in a variable called die_roll.

The third line needs to print the value of die_roll

<div class='hint'>In the previous exercise you imported the <code>sleep</code> function from the <code>time</code> module.</div>
<div class='hint'>In this exercise you need to import the <code>randint</code> function from the <code>random</code> module.</div>
<div class='hint'><code>randint(a, b)</code> will return a random integer between <code>a</code> and <code>b</code> inclusive. </div>
<div class='hint'><code>randint(1, 12)</code> will return a random integer between <code>1</code> and <code>12</code> inclusive. </div>
