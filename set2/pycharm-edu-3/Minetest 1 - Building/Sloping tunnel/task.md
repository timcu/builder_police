# Task 8 - Sloping tunnel

Now we are going to continue building the tunnel from task 5 sending it deep underground.
You will find your next task in a chest at the end of the task 5 tunnel.

## Task

Continue glass tunnel down on a diagonal. The centre of the
tunnel floor will go from x1=69, y1=14 to x2=9, y2=46.

## Lesson

To ensure no lava or water leak into tunnel, build the
full tunnel in glass first and then hollow it out with air.
By never having an open end, water and lava can't flow in.

To create a sloping tunnel you have to build it in
segments. You build a new segment for each value of x.
The image below shows three segments several blocks apart.

<img src="tunnel_segments_separate.png" width="100%" />

If you build segments for each value of x then the segments are
joined and you have a continuous tunnel.

<img src="tunnel_segments_joined.png" width="100%" />

<br>
<div class='hint'><code>num_segments</code> needs a formula in terms of x1 and x2 which returns the number of segments in the tunnel.</div>
<div class='hint'><code>num_segments</code> is the number of different values of x</div>
<div class='hint'>Example value of <code>num_segments</code>: If x1 = 7 and x2 = 5 then there will be 3 values of x (7, 6, 5) even though x1 - x2 = 2. </div>
<div class='hint'>The variable <code>x</code> in the <code>for</code> loop is the x position of
tunnel segment as a formula in terms of x1 and i</div>
<div class='hint'>When i = 0, x = 69 ( = x1)</div>
<div class='hint'>When i = 1, x = 68 ( = x1 - 1)</div>
<div class='hint'><div>When i = 2, x = x1 - 2</div>
<div>When i = 3, x = x1 - 3</div>
<div>When i = 4, x = x1 - 4</div>
<div>...</div>
<div>Find the pattern to work out the formula.</div></div>
<div class='hint'>The variable <code>y</code> in the <code>for</code> loop is the y position of tunnel segment floor in terms of y1 and i</div>
<div class='hint'>
<div>When i = 0, y = y1</div>
<div>When i = 1, y = y1 - 1</div>
<div>When i = 2, y = y1 - 2</div>
<div>When i = 3, y = y1 - 3</div>
<div>When i = 4, y = y1 - 4</div>
<div>Find the pattern to work out the formula.</div></div>
<div class='hint'>The variable <code>z</code> in the <code>for</code> loop is the z position of corner of tunnel segment in terms of <code>ref_z</code> and <code>tunnel_width</code></div>
<div class='hint'><code>ref_z</code> is centre of tunnel so <code>z</code> will be half the tunnel width less than <code>ref_z</code></div>
<div class='hint'><code>range_y_ext range()</code> stop value needs a formula in terms of <code>y</code> and <code>tunnel_height</code> which returns one more than the highest value of <code>y</code> for glass in this tunnel at position <code>i</code>.</div>
<div class='hint'><code>range_z_ext range()</code> stop value needs a formula in terms of <code>z</code> and <code>tunnel_width</code> which returns one more than the highest value of <code>z</code> of the glass in the tunnel.</div>
<div class='hint'><code>range_z_floor</code> can be a tuple of numbers <code>(0, 1, 2, 3)</code>, a list of numbers <code>[0, 1, 2, 3]</code>, or a range of numbers <code>range(4)</code>.</div>
<div class='hint'><code>range_z_floor range()</code> sequence needs to provide all the values of z for the stone floor.</div>
<div class='hint'><code>range_z_floor range()</code> should return 3 values</div>
<div class='hint'><code>range_z_floor range()</code> sequence numbers can be as formulae in terms of z or ref_z, or just as numbers</div>
<div class='hint'>Formulae for <code>x, y, z</code> in the second <code>for</code> loop are same as the formulae in the first <code>for</code> loop.</div>
<div class='hint'><code>range_y_air range()</code> stop value needs a formula in terms of <code>y</code> and <code>tunnel_height</code> which is one more than the vertical position of the highest air block in segment <code>i</code> of the tunnel.</div>
<div class='hint'><code>range_z_air</code> is the same as <code>range_z_floor</code></div>
<div class='hint'>The <code>if</code> statement needs a condition that is only <code>True</code> for every fourth value of <code>i</code></div>
<div class='hint'>Use modulo operator <code>%</code> on <code>i</code> to check for every fourth value of <code>i</code></div>
<div class='hint'>The boolean expression (condition) <code>i % 4 == 0</code> returns <code>True</code> for every fourth value of <code>i</code></div>
<div class='hint'>When placing a torch the <code>y</code> value needs to be that of one block above floor at position <code>i</code> of tunnel in terms of <code>y</code></div>
<br>
