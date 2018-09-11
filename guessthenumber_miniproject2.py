# Mini-project #2 - "Guess the Number!"

# Project template: http://www.codeskulptor.org/#examples-guess_the_number_template.py

# CodeSkulptor submission link: http://www.codeskulptor.org/#user45_XHF5nguKNXoX9o9_26.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code
    global secret_number, guess_rem
    secret_number = random.randrange(0,range_max)
    guess_rem = int(math.ceil(math.log(range_max+1)/math.log(2)))
    print ""
    print "New game!"
    print "Guess a number between 0 and", range_max
    print "You have", guess_rem, "guesses remaining."

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code
    global range_max
    range_max = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_max
    range_max = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    guess_num = int(guess)
    
    print ""
    print "Guess was", guess_num
    
    global guess_rem
    
    if secret_number > guess_num:
        if guess_rem == 1:
            print "You are out of guesses! Sorry, you lose!"
            new_game()
        else:
            print "Guess higher."
            guess_rem -= 1
            print "You have", guess_rem, "guesses remaining." 
    elif secret_number < guess_num:
        if guess_rem == 1:
            print "You are out of guesses! Sorry, you lose!"
            new_game()
        else:
            print "Guess lower."
            guess_rem -= 1
            print "You have", guess_rem, "guesses remaining." 
    else:
        print "Correct! You win!"
        new_game()
        

    
# create frame
frame = simplegui.create_frame("Guess the Number!", 100, 200)

# register event handlers for control elements and start frame
frame.add_input("Guess:", input_guess, 100)
frame.add_button("Range is [0, 100)", range100)
frame.add_button("Range is [0, 1000)", range1000)
frame.start()

# call new_game
range_max = 100
new_game()


# always remember to check your completed program against the grading rubric
