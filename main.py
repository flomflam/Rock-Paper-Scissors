# Rock Paper Scissors starter code

#a library that will help with having the "computer" choose
import random

# User Input to choose "rock", "paper" or "scissors"

#a variable (named list) that holds all 3 options to pick from
list = ['rock', 'paper', 'scissors']

#a variable (named user_input) to hold the user's response
user_input = ''

#a function to request the user's response
user_input = input("Select rock, paper, or scissors: ")

#prints the input received from the user
print(user_input)

# Repeat user input if not in the options (variable named list)
while user_input not in list:
    user_input = input("Select rock, paper, or scissors: ")
    print(user_input)

# Randomly pick computer choice
#a variable (named computer_input) to hold the computer's random response
computer_input = ''

#using the choice function from the random library
#the function randomly selects an element from the given sequence
computer_input = random.choice(list)
#prints the random choice for the computer
print(computer_input)

# Apply game rules (determine winner or tie)
# Print message with choices and result

## Nice-to-have
# ask user for number of games
# ask user to play another game at the end
# for multiple games keep score and announce winner at the end


#code snippets that may come in handy
"""
while a < b:
  print("this is a loop"

if a:
  print("a is true and a can be a single thing, or a statement")
else:
  print("a must not be true")

"""