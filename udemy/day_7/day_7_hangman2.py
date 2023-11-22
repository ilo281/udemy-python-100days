#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
print(chosen_word)

guess = input("Guess a letter \n").lower()

letter_exist = False
for letter in chosen_word:
    if letter == guess:
        letter_exist = True
print("letter exist", letter_exist)

# This works but only selects first element
for letter in chosen_word:
    display.append("_")
    if guess == letter:
        display[chosen_word.index(letter)] = guess
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)







