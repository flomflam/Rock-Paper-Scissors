# Rock Paper Scissors starter code

#a library that will help with having the "computer" choose
import random

#a variable (named list) that holds all 3 options to pick from
list = ['rock', 'paper', 'scissors']

def play_game():
    user_input = get_user_input()
    computer_input = get_computer_input()
    print("You chose", user_input, "and the computer chose", computer_input)
    determine_winner(user_input, computer_input)
    play_again()


def get_user_input():
    user_input = ''
    user_input = input("Select rock, paper, or scissors: ")

    #prints the input received from the user
    print(user_input)

    # Repeat user input if not in the options (variable named list)
    while user_input not in list:
        user_input = input("Select rock, paper, or scissors: ")
        print(user_input)

    return user_input


def get_computer_input():
    # Randomly pick computer choice
    #a variable (named computer_input) to hold the computer's random response
    computer_input = ''

    #using the choice function from the random library
    #the function randomly selects an element from the given sequence
    computer_input = random.choice(list)
    #prints the random choice for the computer
    print(computer_input)

    return computer_input


def determine_winner(user_input, computer_input):
# Apply game rules (determine winner or tie)
# Print message with choices and result
    if user_input == computer_input:
        print("It's a tie!")
    elif user_input == 'rock':
        if computer_input == 'scissors':
            print("rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == 'paper':
        if computer_input == 'rock':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == 'scissors':
        if computer_input == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

def play_again():
    play_again_options =['Y', 'y', 'N', 'n']
    play_again_input=input("Play again? (y/n): ")
    while play_again_input not in play_again_options:
        play_again_input = input("Play again? (y/n): ")
    if play_again_input.lower() != "n":
            play_game()  
        
        
    
play_game()


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
