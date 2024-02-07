import random
from hangman_words import word_list
from hangman_art import stages, logo


chosen_word = random.choice(word_list)
display = []
print(chosen_word)

lives = 6

game_over = False
print(logo)
for letter in chosen_word:
    display.append("_")
print(display)
guess_counter = 0
while not game_over:
    guess = input("Guess a letter \n").lower()
    if guess in display:
        print(f"you already guessed this letter {guess}")
    else:
        print(f"a letter is not in word {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            guess_counter += 1
            display[position] = letter
    if letter != guess:
        lives -= 1
    if lives == 0:
        print("you lose")
        game_over = True
    print(display)

    # Join all the elements in the list and turn it into a String.
    if not lives == 0:
        for element in display:
            if element == "_":
                game_over = False
            if element != "_" and guess_counter == len(chosen_word):
                game_over = True
        if game_over:
            print("you won")

    print(stages[lives])