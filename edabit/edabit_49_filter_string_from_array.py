#1 create a function which takes list of strings and integers
#2 filter list so that it returns list of integers only
def filter_list(list_of_strings_and_integers):
    output_list = []
    for character in list_of_strings_and_integers:
        if type(character) is int:  # determine type of item
            output_list.append(character)

    return output_list


print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))
print(filter_list(["Nothing", "here"]))
