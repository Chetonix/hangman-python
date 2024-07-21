from hangman_words import word_list
from hangman_art import stages, logo
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(chosen_word)

game_end = False
lives = 6

print(logo)

display = []
for _ in chosen_word:
    display += "_"


while(not game_end):
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have guessed the letter '{guess}' already.")

    for pos in range(word_length):
        ch = chosen_word[pos]
        if guess == ch:
            display[pos] = ch

    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word.")
        lives -= 1

    if lives == 0:
        game_end = True
        print(f"You lose, the word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("You win.")

    print(stages[lives])
