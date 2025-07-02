# Create a function that takes a string and returns True or False,
# If characters in order return  True if not return False

def is_in_order(input_string):
    ordered_string = False
    sorted_input_string = sorted(input_string)
    print("sorted_input_string", sorted_input_string)
    input_string_as_list = []
    for i in input_string:
        input_string_as_list.append(i) # append function convert string to list
    print("input_string_as_list", input_string_as_list)
    if input_string_as_list == sorted_input_string:
        ordered_string = True
    return ordered_string


print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz"))
