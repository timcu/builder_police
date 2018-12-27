# Data types

We will start off with some Python tasks which do not use Minetest.

## Task

Fill in the five missing code fragments in the program on the left.
When you run it, pay attention to the printed output which displays in the
"Run" pane at the bottom of this window.

## Lesson

This lesson looks at more detail at some variable data types we
have used before. The best way to learn about data types is 
to experiment with them in the Python Console which can be 
found in the tab at the bottom of this window. Open up the Python 
Console by clicking on the tab. You can type the examples
below directly in the console. On the right of the console
is a window which shows the value of any variables you
have created.

For example, type `a="cat"` in the console
and on the right you will see `a = {str} 'cat'`</p>

Now type `a+="cher"` and on the right you will
see `a = {str} 'catcher'`

## Tuples
The first data type is a tuple, which is an immutable
group of data surrounded by parentheses.

        # Examples
        t1 = (3, 4, 12)         # three integers
        t2 = ("three", "four")  # two strings
        t3 = (1.23, 45, "cat")  # a decimal number, an integer and a string
        t4 = (t1, (5, 6, 30))   # two tuples

Immutable means that once the tuple has been created,
you can't change any element in the tuple. This makes 
programming with tuples less prone to errors than programming with lists
which are mutable. (Lists are designated by square brackets 
`[3, 4, 12]`).

Individual elements of a tuple are accessed by index value. For example

        t1[0]  # should display 3
        t1[1]  # should display 4
        t1[2]  # should display 12

You can also assign elements to multiple variables in a single statement.

        x, y, z = t3
        x  # should display 1.23
        y  # should display 45
        z  # should display 'cat'

<br>
<div class='hint'>Strings must be surrounded by single quotes or double quotes</div>
<div class='hint'>int is the python term for integer</div>
<div class='hint'>float is the python term for decimal number or floating point number</div>
<div class='hint'>string is the python term for text</div>
<div class='hint'>Tuple indexes are zero based so the first element has index 0</div>
<br>
