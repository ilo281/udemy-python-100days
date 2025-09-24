# Create a function that takes a number as an argument and returns True or False
# Depending on whether the number is summetrical or not return True or False

def is_symmetrical(number_in) -> bool:
    number_is_symmetrical = False
    number_to_string = str(number_in)
    string_to_list = []
    for item in number_to_string:
        string_to_list.append(item)

    negative_counter = -1
    for i in range(0, len(string_to_list)):
        if string_to_list[i] == string_to_list[negative_counter]:
            number_is_symmetrical = True
            negative_counter -= 1
        else:
            number_is_symmetrical = False
            break

    return number_is_symmetrical


print(is_symmetrical(7227))
print(is_symmetrical(12567))
print(is_symmetrical(44444444))
print(is_symmetrical(9939))
print(is_symmetrical(1112111))
