# 1 create a function which will return integer
# 2 which calculate total number of characters
# 3 return 0 if the given list is empty
def count_characters(list_of_strings):
    number_of_characters = 0
    total_characters = 0
    if not list_of_strings:
        number_of_characters = 0
    if list_of_strings:
        for string in list_of_strings:
            number_of_characters = len(string)
            total_characters = total_characters + number_of_characters

    return total_characters


print(count_characters(["###", "###", "###"]))
print(count_characters(["22222222", "22222222"]))
print(count_characters(["------------------"]))
print(count_characters([]))
print(count_characters(["", ""]))
