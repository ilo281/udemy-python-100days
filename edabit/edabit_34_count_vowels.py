def count_vowels(input_string):
    # 1 find if a letter is vowel
    # 2 count them
    list_of_vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for letter in input_string:
        if letter in list_of_vowels:
            vowel_counter = vowel_counter + 1
    return vowel_counter


my_string = "Celebration"
print(count_vowels(my_string))
my_string = "Palm"
print(count_vowels(my_string))
my_string = "Prediction"
print(count_vowels(my_string))


def my_vowels_counter():
    vowels_printer = count_vowels("Palm")
    print(vowels_printer)


my_vowels_counter()




