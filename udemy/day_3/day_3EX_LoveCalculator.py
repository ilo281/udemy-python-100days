print("Welcome to the the Love Calculator!")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")

combined_names = name1 + name2

lower_case_names = combined_names.lower()
letter_count = 0
word_true = "true"
for letter in word_true:
    true_counter = letter_count + lower_case_names.count(letter)

word_love = "love"
letter_count = 0
for letter in word_love:
    love_counter = letter_count + lower_case_names.count(letter)
digits_counter = f"{true_counter}{love_counter}"
print(digits_counter)

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


