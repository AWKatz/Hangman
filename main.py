# Day 7 of 100 for the Udemy Python Bootcamp
import random
from turtle import clear

import hangman_art
import hangman_words

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
#print(f"Debug: {chosen_word}")

# Get the length of the word and store it
word_length = range(len(chosen_word))

# Title!
print(hangman_art.logo)

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in word_length:
    display += "_"

# This wasn't part of the daily lesson, but I added it for playability
# Show how many letters are in the word before the player is asked to guess
print(f"Your Word = {''.join(display)}")

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
# Set number of lives
lives = 6

while end_of_game == False:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Pick a letter:\n").lower()

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #for letter in chosen_word:
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    #    if letter == guess:
    #        print("Matched.")
    #    else:
    #        print("Not Matched.")

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for position in word_length:
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the letter at that position doesn't match 'guess' then reveal remove a life.
    if guess not in chosen_word:
        lives -= 1
        # Check if the users lives reached 0.
        if lives == 0:
            print("\nYOU LOSE!")
            # This wasn't part of the daily lesson, but I added it for playability
            print(f"The word was: {chosen_word}")
            end_of_game = True

        # If the user has repeated a guess, let the user know.
        if guess in display:
            print(f"\nYou've already guessed {guess}")
        # If the guess isn't in the word_choice, let the user know.
        if guess not in chosen_word:
            print(f"\n{guess} is not in the word")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    # Display ASCII art and tell the player how many more guesses they have left.
    print(hangman_art.stages[lives])
    print(f"Lives Remaining: {lives}")

