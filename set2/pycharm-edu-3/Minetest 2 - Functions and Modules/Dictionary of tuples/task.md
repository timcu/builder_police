# Dictionary of Tuples

Now we combine the previous two lessons to discover the usefulness of a `dict` with `tuple` keys.

## Task

Complete the seven missing code fragments. Run the program and study the printed output.

## Lesson

Because tuples are immutable, they can be used as
keys in a `dict` (dictionary). This is useful when storing our `node_dict`. It means if we set a data value
in a `dict` with coordinates that have already been used it will replace the previous setting.
If there is no previous setting then a new "key:value" pair will be added to the dictionary.

Try the task on the left and see if you can predict
what `node_dict` will look like after each step.

At the end is a `for` loop which
checks different formulae for a set of data. 
This is a way of evaluating which is the right
formula to use. For each value of `z`, write down
what you think the correct integer should be
and then see which formula gives the same answers.
You are looking for a formula which returns the 
`z` value of the centre of a block given the `z` value
of any part of the block.

<br>
<div class='hint'>Enter x, y, z coordinates as three numbers in tuple to be key for dictionary where value is "default:wood"</div>
<div class='hint'>Set the value of node_dict item with index of (16, 20, 10) to "default:glass" using
<pre><code>node_dict[(16, 20, 10)] = "default:glass"</code></pre></div>
<div class='hint'>To set items within the <code>for z</code> loop, use the same statement as before with "default:stone" as the material and the z coordinate in terms of the variable <code>z</code></div>
<div class='hint'>See previous task description if you have forgotten how to remove a node</div>
<div class='hint'>Use built-in function <code>del()</code> to delete an item from dict</div>
<div class='hint'>To remove node at (x, y, z) use <code>del(node_dict[(x, y, z)])</code></div>
<div class='hint'><div>To convert <code>float</code> to an <code>int</code> use a formula in terms of z from the table created by the <code>for i</code> loop.
The requirements are:</div>
<div><code>float</code>s in the range <code>&nbsp;9.51</code> to <code>10.49</code> will resolve to <code>int</code> of <code>10</code></div>
<div><code>float</code>s in the range <code>-1.49</code> to <code>-0.51</code> will resolve to <code>int</code> of <code>-1</code></div>
<div><code>float</code>s in the range <code>-0.49</code> to <code>&nbsp;0.49</code> will resolve to <code>int</code> of <code>&nbsp;0</code></div>
<div><code>float</code>s in the range <code>&nbsp;0.51</code> to <code>&nbsp;1.49</code> will resolve to <code>int</code> of <code>&nbsp;1</code></div></div>
<br>
