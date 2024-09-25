def name_shuffle(input_string):
    # Function split input string on space . Create new string with swapped parts
    new_list = input_string.split(" ")

    return new_list[1] + " " + new_list[0]


print(name_shuffle("Donald Trump"))

print(name_shuffle("Rosie O'Donnell"))

print(name_shuffle("Seymour Butts"))
