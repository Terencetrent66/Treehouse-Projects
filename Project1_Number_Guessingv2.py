"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    welcome = (" Welcome to the Number Guessing Game!")
    welcome_length=(len(welcome)+3)
    border = print("*"* welcome_length)
    print(welcome)
    border = print("*"* welcome_length)
    attempt_count = 0
    correct_answer = random.randint(1,10)
    high_score = [10]
    print(correct_answer)
    while attempt_count > -1:
        try:
            user_answer = int(input("\nPlease pick a number between 1 and 10:  "))
            if user_answer not in range(1,11):
                print("Sorry, that mumber is not between 1 and 10.  Please try again.")
                continue
            if user_answer > correct_answer:
                print("Sorry, that is is higher than correct number.  Please try again.")
                attempt_count += 1    
            if user_answer < correct_answer:
                print("Sorry, that is is lower than correct number.  Please try again.")
                attempt_count += 1
            if user_answer == correct_answer:
                attempt_count += 1
                high_score.append(attempt_count)
                new_high_score = min(high_score)
                print("\nGot it! You guessed correctly.")
                print("It took {} attempts".format(attempt_count))
                print("The highest score is {} attempts.".format(new_high_score))
                play_again = input("This game is over.  Would you like to play again? (Y/N)"  )
                play_again = play_again.lower()
                if play_again == "y":
                    attempt_count=0
                    correct_answer = random.randint(1,10)
                    print(correct_answer)
                    continue   
                if play_again == "n":
                    print("Thanks for playing.  Have a nice day!")
                    break
        except ValueError:
            print("Oh no!  That is not a number between 1 and 10.  Try again...")
        
                     

      
start_game()
