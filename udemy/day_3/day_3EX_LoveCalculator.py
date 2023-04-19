print("Welcome to the the Love Calculator!")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")

combined_names = name1 + name2

lower_case_names = combined_names.lower()
letter_count = 0
all_true_letters_counter = 0
word_true = "true"
for letter in word_true:
    true_counter = letter_count + lower_case_names.count(letter)
    all_true_letters_counter = all_true_letters_counter + true_counter

word_love = "love"
all_love_letters_counter = 0
letter_count = 0
for letter in word_love:
    love_counter = letter_count + lower_case_names.count(letter)
    all_love_letters_counter = all_love_letters_counter + love_counter
digits_counter = int(f"{all_true_letters_counter}{all_love_letters_counter}")


if (digits_counter < 10) or (digits_counter > 90):
    print(f"your score is {digits_counter} , you go together like coke and mentos ")
elif (digits_counter >= 40) and (digits_counter <= 50):
    print(f"your score is {digits_counter},you are alright together")
else:
    print(f"your score is {digits_counter}")


# lower_case.count("u")
# lower_case.count("e")
#
# true = t + r + u +e
#
# lower_case.count("l")
# lower_case.count("o")
# lower_case.count("v")
# lower_case.count("e")
#
# love = l + o + v + e
#
# love_score = str(true) + str(love)
#
# print("your score is x , you go together like coke and mentos ")
#
# print("your score is y, you are alright together ")

#print("your score is z ")





#lower_case_name = name1.lower()
#lower_case_name.count("true")
#lower_case_name.count("love")


