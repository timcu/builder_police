<html>
<h2>Dictionaries</h2>
<p>A dictionary is a mutable group of data elements that are accessed by keys rather than their numeric
position in the dictionary. The data type is named after the book by the same name because in the book 
the word is the key and the meaning is the data element. You can only have one data element per key
although that data element could be a complex data type such as a tuple, list or another dictionary.
To create a dictionary, the keys and values are separated by colons (:) and the "key:value" pairs are 
separated by commas. Try the following examples in the console</p>
<div><code>d1={'score':25, 'another':'mine', 43:'numeric key', 'secret':"don't look"} # creates dict</code></div>
<div><code>d1['secret'] # should display "don't look"</code></div>
<div><code>d1['another']='dog' # assigns new value for existing key</code></div>
<div><code>del(d1[43]) # removes data element with key 43 </code></div>
<div><code>del(d1['secret']) # removes data element with key 43 </code></div>
<div><code>d1['height']=180 # adds a new data element and key</code></div>
<div><code>d1 # {'score': 25, 'another': 'dog', 'height': 180}</code></div>
<div><code>for k,v in d1.items(): print("key=",k," value=",v) # loops through key:value pairs</code></div>
<div><code>d1={} # creates an empty dictionary</code></div>
<div><code>di=dict() # alternative method of creating empty dictionary</code></div>
<br>
<div class='hint'>Dictionaries are denoted by curly braces</div>
<div class='hint'>A dictionary with keys and values looks like

{'another':'mine', 'secret':"don't look"}</div>
<div class='hint'>Assign a score of 10 to andy</div>
<div class='hint'>key should be 'andy'</div>
<div class='hint'>value should be 10</div>
<div class='hint'>dictionary to use is stored in variable scores</div>
<div class='hint'>scores[key] = value</div>
<div class='hint'>Set value of 15 for key 'betty'</div>
<div class='hint'>set value of 12 to key 'cathy'</div>
<div class='hint'>Get andy's score, add 3, and save it back in scores dictionary</div>
<div class='hint'>function to return all the key:value pairs of data in a for loop</div>
<div class='hint'>function is a method of the dict class</div>
<div class='hint'>to run class method on scores use 

scores.<i>function_name</i>()</div>
<div class='hint'>items() is the name of the function to run on the scores object</div>
<div class='hint'>the variable name holding the current score as looping through scores items.</div>
<div class='hint'>the variable name holding the current score as looping through scores items.</div>
<div class='hint'>the variable name holding the current player's name as looping through scores items.</div>
<br>
