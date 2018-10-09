<html>
<h3>Lesson</h3>
<p>Python provides a <b>range</b> function which is easier to use than typing every value in a sequence.
The <b>range</b> function has up to three arguments giving the start value, the end value and the
increment value. Note that range includes up to but not including the end value. If you don't
provide an increment it is assumed to be 1. If you don't provide a start value it is assumed to 
be 0. If you only provide two values they are assumed to be start value and end value. 
If you only provide one value it is assumed to be end value</p>

<code style='margin-left:2em;'>range(3)         # equivalent to (0, 1, 2)</code><br />
<code style='margin-left:2em;'>range(2, 5)      # equivalent to (2, 3, 4)</code><br />
<code style='margin-left:2em;'>range(4, 0)      # equivalent to ()</code><br />
<code style='margin-left:2em;'>range(4, 0, -1)  # equivalent to (4, 3, 2, 1)</code><br />

<h3>Program</h3>
<p>Count down from 20 to 1 before blast off</p>
<h3>Task</h3>
<p>Enter the correct parameters in the <b>range</b> function to count down from 20 to 1</p>

</html>
