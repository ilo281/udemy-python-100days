import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
print(chosen_word)
game_over = False
for letter in chosen_word:
    display.append("_")
print(display)
guess_counter = 0
while not game_over:
    guess = input("Guess a letter \n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            guess_counter += 1
            display[position] = letter
    print(display)
    for element in display:
        if element == "_":
            game_over = False
        if element != "_" and guess_counter == len(chosen_word):
            game_over = True
    if game_over:
        print("you won")
