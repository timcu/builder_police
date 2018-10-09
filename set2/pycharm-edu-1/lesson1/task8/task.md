<style>
.reserved {color: blue; font-weight:bold;}
.comment {color: gray; font-style: italic;}
.subs {color: gray; font-style: italic;}
.indent {margin-left:2em; }
.indent2 {margin-left:4em; }
</style>
<h3>Lesson</h3>
<p>Previously we looked at <code>for</code> loops which repeat the 
same lines of code a fixed number of times. Another loop structure is 
the <code>while</code> loop which will repeat the lines of code while some 
condition is <code>True</code>.</p>
<div><code class="indent">while</code> <code class="subs">condition:</code></div>
<div><code class="indent2"># lines of code</code></div>
<div><code class="indent2"># which are to be repeated</code></div>
<div><code class="indent2"># all indented the same amount</code></div>
<p><code class="subs">condition</code> is often of the form</[>
<div class="indent"><code class="subs">value1 operator value2</code></div>
<p>where <code class="subs">operator</code> is one of the following</p>
<code class="indent">== # value1 equals value2</code><br />
<code class="indent">!= # value1 does not equal value2</code><br/>
<code class="indent">&lt; &nbsp;# value1 is less than value2</code><br/>
<code class="indent">&gt; &nbsp;# value1 is greater than value2</code><br/>
<code class="indent">&lt;= # value1 is less than or equal to value2</code><br/>
<code class="indent">&gt;= # value1 is greater than or equal to value2</code><br/>
<p>The <code>if</code> statement is similar to the <code>while</code> statement but only executes
once the indented lines which follow. 
<code>if elif else</code> can be used to check several conditions with different responses
for each condition.</p>
<code class="indent">if condition1:</code><br/>
<code class="indent2"># What to do if condition1 is True</code><br/>
<code class="indent">elif condition2:</code><br/>
<code class="indent2"># What to do if condition1 is False and condition2 is True</code><br/>
<code class="indent">elif condition3:</code><br/>
<code class="indent2"># What to do if condition1 and condition2 are False and condition3 is True</code><br/>
<code class="indent">else</code><br/>
<code class="indent2"># What to do if all conditions are False</code><br/>
<p>This program also introduces the <code>input</code> function to get string data from the user. The <code>int</code>
function converts it to an integer number so that the program can compare it to the answer.</p>
<div class="indent"><code># Use input function to get the guess from the user (as a string)</code></div>
<div class="indent"><code>s=input("Guess?")</code></div>
<div class="indent"><code># Check that guess is an integer by surrounding in try: except ValueError: else:</code></div>
<div class="indent"><code>try:</code></div>
<div class="indent2"><code># Convert from string to integer. If it can't be converted, </code></div>
<div class="indent2"><code># jump to "except ValueError". Otherwise jump to "else"</code></div>
<div class="indent2"><code>guess=int(s)</code></div>
<div class="indent"><code>except ValueError:</code></div>
<div class="indent2"><code># Entered value can not be converted to integer</code></div>
<div class="indent2"><code>print("Your guess of '" + s + "' is not an integer (whole number). Please only enter integers.")</code></div>
<div class="indent"><code>else:</code></div>
<div class="indent2"><code># Code in the else: only runs if there was no error in the try: section (converting to integer)</code></div>


<h3>Program</h3>
<p>Asks user to guess a random number between 0 and 63 and then gives clues until user guesses the number<p>

<h3>Task</h3>
<p>Enter the correct operator in each of the conditional statements so program will stop when answer is correctly guessed. Also need to enter the correct conditions 
so the program responds correctly after each guess</p>
