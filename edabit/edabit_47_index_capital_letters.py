# 1 Create a function that take a string as argument .
# 2 This function should return list
# 3 This list need to ordered and  contain the indices of all capital letters in the string
#  append function is simple   way to populate  list

def index_of_caps(string_in):
    list_out = []
    for letter in string_in:
        capital_letter = letter.isupper()
        if capital_letter:
            index_of_capital_letter = string_in.index(letter)
            list_out.append(index_of_capital_letter)

    return list_out


print(index_of_caps("eDaBiT"))
print(index_of_caps("determine"))
print(index_of_caps("eQuINoX"))
print(index_of_caps("STRIKE"))
print(index_of_caps("sUn"))
