# Dictionaries

You will now learn about the `dict` data type which is the Python
name for a dictionary. `dict`s are a powerful programming tool
which enable Python programs to achieve a lot in a few lines of code.
This exercise also does not use Minetest, but is necessary to be able to complete the
"Railway station" exercise.

## Task

Complete the nine missing code fragments in the program on the left.
Pay attention to the printed output after running the program.

## Lesson

A dictionary is a mutable group of data elements that are accessed by keys rather than their numeric
position in the dictionary. The data type is named after the book by the same name because in the book 
the word is the key and the meaning is the data element. You can only have one data element per key
although that data element could be a complex data type such as a tuple, list or another dictionary.
To create a dictionary, the keys and values are separated by colons (:) and the "key:value" pairs are 
separated by commas. Try the following examples in the console

        d1={'score':25, 'another':'mine', 43:'numeric key', 'secret':"don't look"}  # creates dict
        d1['secret']  # should display "don't look"
        d1['another']='dog'  # assigns new value for existing key
        del(d1[43])  # removes data element with key 43
        del(d1['secret'])  # removes data element with key 43
        d1['height']=180  # adds a new data element and key
        d1  # {'score': 25, 'another': 'dog', 'height': 180}
        for k,v in d1.items(): print("key=",k," value=",v)  # loops through key:value pairs
        d1={}  # creates an empty dictionary
        d1=dict()  # alternative method of creating empty dictionary

<br>
<div class='hint'>Dictionaries are denoted by curly braces <code>{}</code></div>
<div class='hint'>A dictionary with keys and values looks like
<code>{'another':'mine', 'secret':"don't look"}</code></div>
<div class='hint'>To assign a score of 100 to danny use the following
<pre><code>    scores['danny'] = 100</code></pre></div>
<div class='hint'>To add 3 to andy's score, get andy's score, add 3, and save it back in <code>scores</code> dictionary</div>
<div class='hint'>To complete the <code>for</code> loop, enter a function to return all the key:value pairs of data in scores</div>
<div class='hint'><code>items()</code> is the name of the function to run on the <code>scores</code> to get all key:value pairs <code>scores.items()</code></div>
<br>
