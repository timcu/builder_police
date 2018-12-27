<html>
<h2>Dictionary of Tuples</h2>
<p>Because tuples are immutable, they can be used as
keys in a Dictionary. This is useful when storing our nodes_dict. It means if we set a data value
in a dictionary with coordinates that have already been used it will replace the previous setting. 
If there is no previous setting then a new "key:value" pair will be added to the dictionary.</p>
</p>
<p>Try the task on the left and see if you can predict
what <code>nodes_dict</code> will look like after each step.
</p>
<p>
At the end is a <code>for</code> loop which 
checks different formulae for a set of data. 
This is a way of evaluating which is the right
formula to use. For each value of z, write down
what you think the correct integer should be
and then see which formula gives the same answers.
You are looking for a formula which returns the 
z value of the centre of a block given the z value
of any part of the block.
</p>

<br>
<div class='hint'>First element of tuple</div>
<div class='hint'>value of x coordinate</div>
<div class='hint'>Second element of the tuple</div>
<div class='hint'>value of y coordinate</div>
<div class='hint'>Third element of tuple</div>
<div class='hint'>value of z coordinate</div>
<div class='hint'>Set the value of nodes_dict item with index of (16, 20, 10) to "default:glass"</div>
<div class='hint'>Assign nodes_dict item to stone
</div>
<div class='hint'>Tuple for index is in terms of z
</div>
<div class='hint'>(16, 20, z)</div>
<div class='hint'>Use built-in function to delete an item from dict</div>
<div class='hint'>del()
</div>
<div class='hint'>see previous task description if you have forgotten how to remove a node</div>
<div class='hint'>formula in terms of z</div>
<div class='hint'>ensure floats in the range 9.51 to 10.49 will resolve to int of 10
</div>
<div class='hint'><div>ensure floats in the range -1.49 to -0.51 will resolve to int of -1</div>
<div>ensure floats in the range -0.49 to 0.49 will resolve to int of 0</div> 
<div>ensure floats in the range 0.51 to 1.49 will resolve to int of 1</div></div>
<br>
