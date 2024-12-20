# A SIMPLE GAME WHERE THE USER HAS TO GUESS A RANDOMLY GENERATED NUMBER.

import random

def guessing_game():
    number_to_guess = random.randint(1,10)
    guess = None
    attempts = 0
    
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
    print(f"Congratulations!!! You guessed the number in {attempts} attempts.")
    
guessing_game()

# MEANING OF EACH LINES 

# line 3, this line imports the random module, which provides functionality for generating random numbers.
# line 5, this line defines a function called guessing_game, which contains the logic for the game.
# line 6, this line generates a random integer between 1 and 10 using the randint function from the random module and it store in number_to_guess.
# line 7, guess: initialized to none, which will store the user's guess.
# line 8, attempts: initialized to 0, which keep track of the number of attempts the user makes.

# line 10, this line starts a while loop that will continue to execute until the user's guess matches the generated number.
# line 11, this line ask user to input the number.
# line 12, this line increments the attempts variable by 1 each time the user makes a guess.
# line 13, 14, 15, 16, provides feedback to the user based on their guess.
# line 17, this line prints a congratulatory message to the user when they correctly guess the number, along with the number of attempts it took them.

# line 19, this line call the function guessing_game i.e, line 5.