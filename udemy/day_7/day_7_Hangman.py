#  Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#  Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#  Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter \n").lower()

letter_exist = False
for letter in chosen_word:
    if letter == guess:
        letter_exist = True
        print("letter", letter)

print("letter exist", letter_exist)
