# Create an empty dictionary called score
scores = dict()

# Assign a score of 10 to a player called andy
scores['andy'] = 10

# Assign a score of 15 to a player called betty
scores['betty'] = 15

# Assign a score of 12 to a player called cathy
scores['cathy'] = 12

# Add 3 to andy's score
scores['andy'] += 3

# Print all the scores
print(scores)

# Find who has the highest scores
max_score = None
winner = None
for name, score in scores.items():
    if not max_score or max_score < score:
        max_score = score
        winner = name
print("Winner is", winner, "with a score of", max_score)


# © Copyright 2018 Triptera Pty Ltd
# https://www.triptera.com.au
# See LICENSE.txt
# Python code in task.py is free to be copied and reused.
# Minetest course may not be copied without permission from Triptera Pty Ltd.
# Minetest course is authorised for use in schools and CoderDojo sessions in 2018 - 2019.
