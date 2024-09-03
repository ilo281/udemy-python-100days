def replace_vowels(input_string, ch): # declared  function

    # 1 find vowels
    # 2 replace with specified characters

    list_of_vowels = ["a", "e", "i", "o", "u"] # created list of vowels
    new_list = list(input_string) # declared variable which creates list from string
    for letter in new_list: # loop through list
        if letter in list_of_vowels: # look for vowel in  the list created after loop
            this_index = new_list.index(letter) # determine index of a letter  in new_list
            new_list[this_index] = ch # replace a character with # based on index
    string_to_return = "".join(new_list) # convert list to string

    return string_to_return


print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))

# add comments to lines of codes
