# Create a tuple with the three integers
t1 = (15, 6, 1234)
print(t1)

# Create a tuple with two strs (str = string = text in Python terminology)
t2 = ("In a galaxy far far away", "there lived a dog")
print(t2)

# Create a tuple with a str, an int and a float
# in that order
t3 = ("My golf handicap", 1, 999.99)
print(t3)

# Print the second element in t1 (should print 6)
print(t1[1])

# Adding tuples creates a new tuple with all the elements
# In the print statement, enter the number of elements you think t5 will have
t5 = t1 + t2
print(t5, " has 5 elements. len(t5)=", len(t5))

# Assign x to the first element in t1,
# Assign y to the second element in t1,
# Assign z to the third element in t1
x, y, z = t1
print("x =", x, " y =", y, " z =", z)


# © Copyright 2018-2021 Triptera Pty Ltd - https://pythonator.com - See LICENSE.txt
