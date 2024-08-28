def replace_vowels(input_string, ch):

    # 1 find vowels
    # 2 replace with specified characters

    list_of_vowels = ["a", "e", "i", "o", "u"]
    new_list = list(input_string)
    for letter in new_list:
        if letter in list_of_vowels:
            this_index = new_list.index(letter)
            new_list[this_index] = ch
    string_to_return = "".join(new_list)

    return string_to_return


print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))

# add comments to lines of codes
