from random import randint
# answer is a randomly generated integer between 0 and 63 inclusive
answer=randint(0,63)
# guess is variable storing user's guess. Initially it is None
guess=None
# guesses is the number of guesses the user has made
guesses=0
print("Guess a number between 0 and 63. (Maximum 10 guesses)")
# 'while' loop repeats the guesses while the condition is True
# In this loop we want to check two conditions and they both have to
# be True for the loop to continue so they are joined with 'and'
#   condition1: user hasn't guessed the correct answer yet
#   condition2: user hasn't exceeded the maximum number of guesses
while guess != answer and guesses < 10:
    guesses+=1
    s=input("Guess?")
    try:
        guess=int(s)
    except ValueError:
        print("Your guess of '" + s + "' is not an integer (whole number). Please only enter integers.")
    else:
        # check if guess is too high
        if guess > answer:
            print("Your guess of " + str(guess) + " is too high")
        # check if guess is too low
        elif guess < answer:
            print("Your guess of " + str(guess) + " is too low")
# The following lines are not included in the 'while' loop because the indentation has returned
# to the same indentation as the 'while' statement. If we are here we know that either 'guess' equals 'answer'
# or guesses is greater than or equal to 10
#
# Check if guess is correct
if guess == answer:
    # Guess is correct
    print("You win: Your guess of ", guess, " matches answer of ", answer)
else:
    # Guess is not correct so must be that guesses is greater than or equal to 10
    print("You lose: Too many guesses")
