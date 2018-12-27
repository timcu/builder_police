<html>
<h1>Data types</h1>
<p>This lesson looks at more detail at some variable data types we 
have used before. The best way to learn about data types is 
to experiment with them in the Python Console which can be 
found in the tab at the bottom of this window. Open up the Python 
Console by clicking on the tab. You can type the examples
below directly in the console. On the right of the console
is a window which shows the value of any variables you
have created.</p>
<p>For example, type <code>a="cat"</code> in the console
and on the right you will see <code>a = {str} 'cat'</code></p>
<p>Now type <code>a+="cher"</code> and on the right you will 
see <code>a = {str} 'catcher'</code></p>
<h2>Tuples</h2>
<p>The first data type is a tuple, which is an immutable
group of data surrounded by parentheses.</p>

<div><code># Examples</code></div>
<div><code>t1 = (3, 4, 12)        # three integers</code></div>
<div><code>t2 = ("three", "four") # two strings</code></div>
<div><code>t3 = (1.23, 45, "cat") # a decimal number, an integer and a string</code></div>
<div><code>t4 = (t1, (5, 6, 30))  # two tuples</code></div>

<p>Immutable means that once the tuple has been created, 
you can't change any element in the tuple. This makes 
programming with tuples less prone to errors than programming with lists
which are mutable. (Lists are designated by square brackets 
<code>[3, 4, 12]</code>).</p>
<p>Individual elements of a tuple are accessed by index value. For example <p>
<div><code>t1[0] # should display 3</code><div>
<div><code>t1[1] # should display 4</code><div>
<div><code>t1[2] # should display 12</code><div>
<p>You can also assign elements to multiple variables in a single statement.</p>
<div><code>x, y, z = t3</code><div>
<div><code>x # should display 1.23</code><div>
<div><code>y # should display 45</code><div>
<div><code>z # should display 'cat'</code><div>

<br>
<div class='hint'>Strings must be surrounded by single quotes or double quotes</div>
<div class='hint'>int is the python term for integer</div>
<div class='hint'>float is the python term for decimal number or floating point number</div>
<div class='hint'>string is the python term for text</div>
<div class='hint'>Tuple indexes are zero based so the first element has index 0</div>
<div class='hint'>Index should be an integer between 0 and 2 inclusive for a tuple of length 3.</div>
<div class='hint'>Enter a number which you think will be the correct number of elements in t5</div>
<div class='hint'>multiple variables can have values assigned in a single equation</div>
<br>
