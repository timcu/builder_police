<style>
table {border-left: 1px solid gray; border-top: 1px solid gray; border-spacing: 0px; }
th, td {border-right: 1px solid gray; border-bottom: 1px solid gray}
</style>
# Modules

When we have a function that we want to call from different
Python programs we put it in a module. We have already seen how modules can
be imported.

This task also teaches Python's conditional expressions which use a ternary operator.

## Task

Complete the seven missing code fragments in the program on the left.
This module has only function definitions so nothing will happen when it is run.
"Check" task will still check you have entered your answers correctly.

## Lesson

A module looks just like a Python program. Just like a Python program,
a Python module is saved in a file
which ends with ".py".

When a
module is imported, any code not in function definitions is run.
We normally don't want this so we only put function definitions 
in a module.

The `build()` function from the previous task has been put into
a module called minetest_helper.py. Now we can use it by importing
it.

In this task we are creating a new function `build_cuboid()` which
replaces the `MinetestConnection.set_nodes()` function
but saves nodes in a node dictionary to be sent more efficiently later
 to minetest as a batch of data.

The second function we are creating, `node_lists_from_node_dict()`,
converts the `node_dict` to one `node_list` per item and
stores them all in another list. Each `node_list` can be used in
`MinetestConnection.set_node_list()`.

The third function, `send_node_lists()`,
 sends each `node_list` to minetest. We have
to give the user of this function a facility to send some items after others.
For example, when creating a tunnel, the air should be done last because
we don't want lava and water flowing into tunnel during construction. Also 
items such as doors which take two nodes but are only specified by one node
should be built after air when it is certain that no blocks exist on those 
nodes. (Programmer needs to have already left air space for the doors).

This task.py is an example of a module that has no executable code when
imported. All the code is in function definitions. 
When we have completed creating these functions, they will be
added to the minetest_helper module for later use.

## Using a `dict` of nodes

When building tunnels we created a lot of glass nodes and then replaced some of
them with stone, some with air and some with torches. We have to work out all
the nodes that have to be set and what the final 
value of the node is going to be. We use the node_dict variable to
store the latest node type for a set of coordinates.

| Command | node_dict |
|:--------|:----------|
| `# initial value` | `{}` |
| `set_node(2, 4, 6, glass)` | `{(2, 4, 6): "default:glass"}` |
| `set_node(2, 5, 6, glass)` | `{(2, 4, 6): "default:glass", (2, 5, 6): "default:glass"}` |
| `set_node(2, 4, 6, stone)` | `{(2, 4, 6): "default:stone", (2, 5, 6): "default:glass"}` |
| `set_node(2, 6, 6, stone)` | `{(2, 4, 6): "default:stone", (2, 5, 6): "default:glass", (2, 6, 6): "default:stone"}` |

When we convert `node_dict` to `node_lists` we get:

        node_lists = {
        "default:glass": [(2,5,6)],
        "default:stone": [(2,4,6), (2,6,6)],
        "air":           [],
        "default:torch": []}

which is in a good format for using `mc.set_node_list()` command.

<br>
<div class='hint'>Choose one form of the import statement to import the <code>build</code> function from the <code>minetest_helper</code> module:
<div><code>import <i>module</i></code></div>
<div><code>import <i>module.submodule</i></code></div>
<div><code>import <i>module</i> as <i>alias</i></code></div>
<div><code>from <i>module</i> import <i>function</i></code></div>
<div><code>from <i>module</i> import <i>submodule</i></code></div>
<div><code>from <i>module.submodule</i> import <i>subsubmodule</i></code></div></div>
<div class='hint'><div><code>step_x</code> is used in <code>range()</code> function to indicate whether
<code>x1</code> is stepping up or down to get to <code>x2</code></div>
<div><code>step_y</code> is used in <code>range()</code> function to indicate whether
<code>y1</code> is stepping up or down to get to <code>y2</code></div>
<div><code>step_z</code> is used in <code>range()</code> function to indicate whether
<code>z1</code> is stepping up or down to get to <code>z2</code></div>
</div>
<div class='hint'>For <code>step_x, step_y, step_z</code> formulae must return 1 to step up and -1 to step down</div>
<div class='hint'>For <code>step_x</code> formulae must be in terms of <code>x1</code> and <code>x2</code>. Similarly for <code>step_y</code> and <code>step_z</code></div>
<div class='hint'>Python has a ternary operator (operator which takes three values) which can be used to create a single line formula for each of <code>step_x, step_y, step_z</code>
<div><code>d = a if b else c</code></div>
means
<div>if <i>b</i> is true then assign the value of <i>a</i> to <i>d</i>. Otherwise assign the value of <i>c</i> to <i>d</i>.</div></div>
<div class='hint'>When using the ternary operator
<div><code>step_x = true_result if condition else false_result</code></div>
The <i>condition</i> can be formula in terms of x1 and x2 which returns <code>True</code> if stepping up or <code>False</code> if stepping down.
The <i>true_result</i> can be 1 for stepping up and the <i>false_result</i> can be -1 for stepping down.
</div>
<div class='hint'>The following statement creates a new list and stores it in the variable called my_list
<div><code>my_list = []</code></div></div>
<div class='hint'>The following statement stores the variable my_list in the dictionary my_dict with key = "mine"
<div><code>my_dict["mine"] = my_list</code></div> </div>
<div class='hint'>The following statement stores a new list in dictionary my_dict with variable my_key having the value of the key
<div><code>my_dict[my_key] = []</code></div></div>
<div class='hint'>In function <code>node_lists_from_node_dict</code> select the node_list using <code>node_lists[str_item]</code> and
initialise to empty list using <code>= []</code> or add new position to the end using <code>.append(pos)</code>.</div>
<div class='hint'>If you have a dictionary of lists called <code>my_dict</code>, then the list with the key equal to <code>"default:glass"</code> is retrieved by
<div><code>my_dict["default:glass"]</code></div></div>
<div class='hint'>Lists have a built-in function <code>append()</code> which adds a value to the end of a list
<div><code>my_list.append((12, 34, 56))</code></div>
appends the <code>tuple (12, 34, 56)</code> to the list stored in variable <code>my_list</code>. </div>
<div class='hint'><code>mc.set_node_list()</code> takes two arguments. List of <code>(x, y, z)</code> coordinates to be set to a block, and the name of the block</div>
<br>
