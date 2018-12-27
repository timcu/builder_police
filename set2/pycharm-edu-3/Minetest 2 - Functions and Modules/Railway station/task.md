<html>
<h1>Railway station</h1>
<p>We have all the helper functions to build 
complex structures quickly saved in the minetest_helper.py
module. Now we can start building them. The first 
structure will be a railway station.</p>
<p>The design of the station will be implemented in a
function. The user of this function will be able
to change the appearance by setting arguments to the function
such as </p>
<ul>
<li>location</li>
<li>length of platform</li>
<li>size of waiting room</li>
<li>building materials</li>
<li>number of storeys (levels)</li>
</ul>
<p>We make life a bit easier for the user by providing defaults 
for arguments which are not set explicitly. This means the user
only has to provide specifications which are different to the 
defaults. The only data which needs to be provided is the 
location of the station. The user needs to pass in a dictionary
for the function to store the built node data before it is
sent to minetest</p>
<p>Try to follow through the function to see how the different
parts of the station are built. There are comments before each
section because it is not obvious from reading set_nodes commands
what is being achieved at each step.</p> 
<p>Once we are finished developing this function we will add
it to minetest_helper.py module so it can be called from other 
functions.</p>
<p>Three level station</p>
<img src="station_3_levels.png" width="100%" />
<p>One level station</p>
<img src="station_1_level.png" width="100%" />
</html>
<br>
<div class='hint'>formula in terms of platform which returns the z coordinate</div>
<div class='hint'>formula in terms of room which returns the value of the height attribute of room if it exists</div>
<div class='hint'>If room['height'] doesn't exist return the default value</div>
<div class='hint'>See function documentation (between """ and """ just after function definition) for default value of room height </div>
<div class='hint'>formula in terms of materials which returns value of materials['station_stair'] if it exists</div>
<div class='hint'>formula in terms of door which returns the value of door without the last two characters</div>
<div class='hint'>Use the slicing notation to get a slice of a string. Test the following in Python console.
<div><code>a = 'abcdefg'</code></div>
<div><code>a[2:5]  #  'cde'</code></div>
<div><code>a[:5]  #  'abcde'</code></div>
<div><code>a[:-1]  # 'abcdef'</code></div>
First number is the start point (inclusive, defaults to 0 if omitted). 
Second number is the end point (exclusive). If second number is negative it counts back from the end.</div>
<div class='hint'>a formula in terms of levels which allows <code>for</code> to loop with <code>level</code> going from zero to one less than the number of levels.</div>
<div class='hint'>formula in terms of station_width and roof_layer which returns the width of the roof at that layer</div>
<div class='hint'>The bottom layer is layer 0 and it increases by one each layer up it goes</div>
<div class='hint'>formula is the same as the layer_width formula used earlier in the code</div>
<br>
