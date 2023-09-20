import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
random_letters = ""
random_symbols = ""
random_numbers = ""
hard_password = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    random_letters += random_char


for char in range(1, nr_symbols + 1):
    random_char = random.choice(symbols)
    random_symbols += random_char


for char in range(1, nr_numbers + 1):
    random_char = random.choice(numbers)
    random_numbers += random_char

password = random_letters + random_symbols + random_numbers

for char in range(1, len(password) + 1):
    random_char = random.choice(password)
    hard_password += random_char

print("easy password", password)
print("hard password", hard_password)







#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

