## Lesson - `while` and boolean expressions
Previously we looked at `for` loops which repeat the
same lines of code a fixed number of times. Another loop structure is
the `while` loop which will repeat the lines of code while some
`condition` is `True`.

    while condition:
        # lines of code
        # which are to be repeated
        # all indented the same amount

The `condition` is any Python expression which can be evaluated to `True` or `False`. These are called boolean expressions.
Common boolean expressions are comparisons of two values. For example:

    while s != 'python':
        s = input('Non-venomous snake (p****n) ?')

The condition is `s != 'python'` which is a comparison of the value stored
in the variable `s` and the literal string `'python'`. The operator "`!=`" is the "does not equal"
operator. It is supposed to vaguely resemble "≠" but be easier to type. This boolean expression will return `True` and hence keep looping until
the user types in the answer `'python'`. Then the boolean expression will return `False`, and the program will continue after the `while` loop.

The `operator` can be one of the following:

        == # left_value equals right_value
        != # left_value does not equal right_value
        <  # left_value is less than right_value
        >  # left_value is greater than right_value
        <= # left_value is less than or equal to right_value
        >= # left_value is greater than or equal to right_value

Multiple conditions can be combined with the logical operators `and` or `or`. The logical operator `not` works on a single condition.

        and  # True if both left_condition and right_condition are True
        or   # True if either left_condition or right_condition are True
        not  # used with a single condition to reverse `True` to `False` or `False` to `True`

When evaluating a `condition` to `True` or `False`, Python has some flexible rules to make coding easier.
`False`, `None`, the number zero, empty strings, empty lists, empty tuples, and other empty containers all evaluate
to `False`. Anything else evaluates to `True`. This means you can write the following code to do a countdown.

    my_list = ['blast off', 'one', 'two', 'three']
    while my_list:            # loops until my_list has no more elements
        print(my_list.pop())  # pop() removes last value from list and returns it

## Lesson - `if`
The `if` statement is similar to the `while` statement but only executes a single time
the indented lines which follow.

`if elif else` can be used to check several conditions with different responses
for each condition.

    if condition1:
        # What to do if condition1 is True
    elif condition2:
        # What to do if condition1 is False and condition2 is True
    elif condition3:
        # What to do if condition1 and condition2 are False and condition3 is True
    else
        # What to do if all conditions are False

## Lesson - `input()`
This program also introduces the `input` function to get string data from the user.
The `int` function converts it to an integer number so that the program can compare
it to the answer.

    # Use input function to get the guess from the user (as a string)
    s=input("Guess?")
    # Check that guess is an integer by surrounding in try: except ValueError: else:
    try:
        # Convert from string to integer. If it can't be converted,
        # jump to "except ValueError". Otherwise jump to "else"
        guess=int(s)
    except ValueError:
        # Entered value can not be converted to integer
        print("Your guess of '" + s + "' is not an integer (whole number). Please only enter integers.")
    else:
        # Code in the else: only runs if there was no error in the try: section (converting to integer)


## Program

Asks user to guess a random number between 0 and 63 and then gives clues until user
guesses the number.

## Task

Enter the correct operator in each of the conditional statements so program will stop when answer is correctly guessed. Also need to enter the correct conditions
so the program responds correctly after each guess.

<div class='hint'>To check the player hasn't guessed the correct answer yet, compare `guess` with `answer` using the "does not equal" operator</div>
<div class='hint'>To check the player hasn't exceeded the maximum number of guesses, compare `guesses` with `10` using the "less than" operator</div>
<div class='hint'>To check if guess is too high, compare `guess` with `answer` using the "greater than" operator</div>
<div class='hint'>To check if guess is too low, compare `guess` with `answer` using the "less than" operator</div>
<div class='hint'>To check if guess is correct, compare `guess` with `answer` using the "equals" operator</div>

