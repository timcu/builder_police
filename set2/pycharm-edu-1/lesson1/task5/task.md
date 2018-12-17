## Lesson
Python provides a `range()` function which is easier to use than typing every value in a sequence.
The `range()` function has up to three arguments giving the start value, the stop value and the
step value. Note that range includes up to but not including the stop value. If you don't
provide a step it is assumed to be 1. If you don't provide a start value it is assumed to
be 0. If you only provide two values they are assumed to be start value and stop value.
If you only provide one value it is assumed to be stop value.

        range(3)         # equivalent to (0, 1, 2)
        range(2, 5)      # equivalent to (2, 3, 4)
        range(4, 0)      # equivalent to ()
        range(4, 0, -1)  # equivalent to (4, 3, 2, 1)

## Program
Count down from 20 to 1 before blast off

## Task
Enter the correct parameters in the `range()` function to count down from 20 to 1

<div class='hint'>The <code>range()</code> function requires up to three parameters, separated by commas</div>
<div class='hint'>First parameter is start value (inclusive, i.e. it is included in the sequence)</div>
<div class='hint'>Second parameter is stop value (exclusive, i.e. it is not included in the sequence)</div>
<div class='hint'>Third parameter is step value. Use a negative number to step down.</div>
<div class='hint'>Third parameter should be -1 is count down by 1 each iteration.</div>
