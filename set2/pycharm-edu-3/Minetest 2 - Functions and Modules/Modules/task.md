<html>
<style>
table {border-left: 1px solid gray; border-top: 1px solid gray}
th, td {border-right: 1px solid gray; border-bottom: 1px solid gray}
</style>
<h1>Modules</h1>
<p>When we have a function that we want to call from different 
python programs we put it in a module. We have already seen how modules can
be imported. A module looks just like a python program. </p>
<p>When a
module is imported, any code not in function definitions is run.
We normally don't want this so we only put function definitions 
in a module.</p>
<p>The <code>build()</code> function from the previous task has been put into
a module called minetest_helper.py. Now we can use it by importing
it.</p>
<p>In this task we are creating a new function <code>build_cuboid()</code> which
replaces the <code>MinetestConnection.set_nodes()</code> function
but saves nodes in a node dictionary to be sent more efficiently later
 to minetest as a batch of data.</p>
<p>The second function we are creating, <code>node_lists_from_node_dict()</code>,
converts the <code>node_dict</code> to one <code>node_list</code> per item and 
stores them all in another list. Each <code>node_list</code> can be used in 
<code>MinetestConnection.set_node_list()</code>.</p>
<p>The third function, <code>send_node_lists()</code>,
 sends each <code>node_list</code> to minetest. We have 
to give the user of this function a facility to send some items after others.
For example, when creating a tunnel, the air should be done last because
we don't want lava and water flowing into tunnel during construction. Also 
items such as doors which take two nodes but are only specified by one node
should be built after air when it is certain that no blocks exist on those 
nodes. (Programmer needs to have already left air space for the doors).</p> 
<p>This task.py is an example of a module that has no executable code when
imported. All the code is in function definitions. 
When we have completed creating these functions, they will be
added to the minetest_helper module for later use</p>
<h2>Using a <code>dict</code> of nodes</h2>
<p>When building tunnels we created a lot of glass nodes and then replaced some of
them with stone, some with air and some with torches. We have to work out all
the nodes that have to be set and what the final 
value of the node is going to be. We use the node_dict variable to
store the latest node type for a set of coordinates.</p>
<p><table cellspacing="0"><tr><th>Command</th><th>node_dict</th></tr>
<tr><td><code># initial value</code></td><td><code>{}</code></td></tr>
<tr><td><code>set_node(2, 4, 6, glass)</code></td><td><code>{(2, 4, 6): "default:glass"}</code></td></tr>
<tr><td><code>set_node(2, 5, 6, glass)</code></td><td><code>{(2, 4, 6): "default:glass",<br> (2, 5, 6): "default:glass"}</code></td></tr>
<tr><td><code>set_node(2, 4, 6, stone)</code></td><td><code>{(2, 4, 6): "default:stone",<br> (2, 5, 6): "default:glass"}</code></td></tr>
<tr><td><code>set_node(2, 6, 6, stone)</code></td><td><code>{(2, 4, 6): "default:stone",<br> (2, 5, 6): "default:glass",<br> (2, 6, 6): "default:stone"}</code></td></tr>
</table>
</p>
<p>When we convert node_dict to node_lists we get:</p>
<p><code>node_lists = {<br />
"default:glass": [(2,5,6)],
"default:stone": [(2,4,6), (2,6,6)],
"air":           [],
"default:torch": []}
</code></p>
<p>which is in a good format for using <code>mc.set_node_list()</code> command.</p>
</html>
<br>
<div class='hint'>Choose one form of the import statement:

<div><code>import <i>module</i></code></div>
<div><code>import <i>module.submodule</i></code></div>
<div><code>import <i>module</i> as <i>alias</i></code></div>
<div><code>from <i>module</i> import <i>function</i></code></div>
<div><code>from <i>module</i> import <i>submodule</i></code></div>
<div><code>from <i>module.submodule</i> import <i>subsubmodule</i></code></div></div>
<div class='hint'>step_x is used in range() function to indicate whether x1 is stepping up or down to get to x2</div>
<div class='hint'>formula must return 1 to step up and -1 to step down</div>
<div class='hint'>formula must be in terms of x1 and x2</div>
<div class='hint'>Python ternary operator
<div><code><i>a</i> if <i>b</i> else <i>c</i></code></div>
means
<div><code>if <i>b</i> is true return <i>a</i></code></div>
<div><code>if <i>b</i> is false return <i>c</i></code></div></div>
<div class='hint'>When using the ternary operator
<div><code><i>true_result</i> if <i>condition</i> else </i>false_result</i></code></div>
The <i>condition</i> can be formula in terms of x1 and x2 which returns True or False.</div>
<div class='hint'>formula in terms of y1 and y2, to return 1 or -1</div>
<div class='hint'>formula in terms of z1 and z2</div>
<div class='hint'>The following statement creates a new list and stores it in the variable called my_list
<div><code>my_list = []</code></div></div>
<div class='hint'>The following statement stores the variable my_list in the dictionary my_dict with key = "mine"
<div><code>my_dict["mine"] = my_list</code></div> </div>
<div class='hint'>The following statement stores a new list in dictionary my_dict with variable my_key having the value of the key
<div><code>my_dict[my_key] = []</code></div></div>
<div class='hint'>Statement should be in terms of the two variables: node_lists and item</div>
<div class='hint'>Find the list for the current item and append the current pos to it.</div>
<div class='hint'>If you have a dictionary of lists called my_dict, then the list with the key equal to "default:glass" is retrieved by
<div><code>my_dict["default:glass"]</code></div></div>
<div class='hint'>Lists have a built-in function append() which adds a value to the end of a list
<div><code>my_list.append((12, 34, 56))</code></div>
appends the tuple (12, 34, 56) to the list stored in variable my_list. </div>
<div class='hint'>Statement should be in terms of the three variables: node_lists, item, pos</div>
<div class='hint'>add key to the list item_list at the end</div>
<div class='hint'>mc.set_node_list() takes two arguments. List of (x, y, z) coordinates to be set to a block, and the name of the block</div>
<div class='hint'>formula in terms of node_lists and item which returns the list of nodes to be set to the value of item</div>
<br>
