# Task 17 - Flag
You have finished the course, but you now you get to build a flag on your castle using
    your own design.

## Task
Build a flag pole and at the top of the flag pole put a flag of your own design.

## Size
Set the values of variables `flag_height` and `flag_width`.
`flag_height` is the  height of the flag measured from the top
of the flag pole to the top of the flag. `flag_width` is measured from
the flag_pole in the x direction. Try to keep them within 21 x 21 blocks.

## Colours
Put all the colours you want to use in the `list` variable `colours`.

    colours = ["wool:green", "wool:blue"]  # to use the two colours green and blue.

Python has a feature called "list comprehension" which makes it easier to create longer lists.
Look it up if you want to find out more about it. Here is an example that creates a list containing
all 15 colours of wool.

    colours = ["wool:" + colour for colour in "white|grey|dark_grey|black|blue|cyan|green|dark_green|yellow|orange|brown|red|pink|magenta|violet".split("|")]

## Stripe width
If you are using more than one colour you can set the `stripe_width` to be used in the flag pattern.

## Pattern
The next step is to choose the pattern you want for your flag. Here are some examples.

### Single colour

    c = 0

### Vertical stripes

    c = x // stripe_width % num_colours

### Horizontal stripes

    c = y // stripe_width % num_colours

### Diagonal stripes

    c = (x + y) // stripe_width % num_colours

or for the other diagonal

    c = (x - y) // stripe_width % num_colours

### Cross centred on centre of flag

    cx = pole_x + flag_length / 2
    cy = flag_y + flag_height / 2
    c = int(min(abs(x-cx), abs(y-cy))) // stripe_width % num_colours


### Squares centred on centre of flag

    cx = pole_x + flag_length / 2
    cy = flag_y + flag_height / 2
    c = int(max(abs(x-cx), abs(y-cy))) // stripe_width % num_colours

### Circles centred on front bottom corner of flag

    cx = pole_x
    cy = flag_y
    c = int(math.sqrt((x-cx)**2 + (y-cy)**2) ) // stripe_width % num_colours

## Flag shape

The shape of the flag can be defined in a function. This program contains
three functions, and you can choose one of them to define your flag shape.
For the very advanced, try creating your own function.

### Rectangle

    if rectangle_flag(x, y):

### Triangle with full length at top of flag pole

    if triangle_top_flag(x, y):

### Half ellipse

    if half_ellipse_flag(x, y):

© Copyright 2018-2023 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
