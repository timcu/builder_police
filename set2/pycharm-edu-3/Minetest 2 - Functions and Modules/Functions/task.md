# Functions

When you need the same code to be used in several places, it
is easier to put that code in a function and then call that function
when it needs to run that code.

## Task

Complete the nine missing code fragments. Run the program and pay attention to the printed output.

## Lesson

Functions are defined used the
`def` command, followed by the function name and then,
in parentheses `()`, the arguments of the function.

In the last task we discovered we needed to convert all
coordinates to integers when adding to `node_dict`. Otherwise new nodes
for the same position would not overwrite the old nodes. That will soon
get tedious so we will create a function `build()` which
does it for us.

`build()` will return a dictionary with the new
node in it. We will merge that with our existing dictionary 
using the `dict` `update()` function which overwrites
existing data when key is the same.

<br>
<div class='hint'>Convert <code>x, y, z</code> in <code>build()</code> function to the <code>int</code> coordinates of the centre point of node using the same formula used in the last task</div>
<div class='hint'>The <code>build()</code> as we have defined takes four parameters. They are x, y, z, and material</div>
<div class='hint'>Example: <code>build(16, 20, 10, "default:glass")</code></div>
<div class='hint'>In the <code>for z</code> loop, The third parameter in the <code>build()</code> function can be the variable <code>z</code></div>
<div class='hint'>Now that <code>build()</code> converts <code>float</code>s to <code>int</code>s, it is fine to pass inexact
floating point x, y, z coordinates directly to <code>build()</code>.
<br>
