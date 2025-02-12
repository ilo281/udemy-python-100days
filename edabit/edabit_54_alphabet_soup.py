# 1 create a function take a string
# 2 return a string with its letters in alphabetical order
def alphabet_soup(input_string):
    sorted_list = sorted(input_string)
    return_string = ''.join(sorted_list)  # convert list to string

    return return_string


print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))
print(alphabet_soup("geek"))
print(alphabet_soup("javascript"))
