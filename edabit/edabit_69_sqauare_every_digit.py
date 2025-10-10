# Create a function that squares every digit of a number.
def square_digits(input_number) -> int:  # declare a function which returns  integer type
    output_number = 0  # declare a new variable which will be equal to 0
    number_to_string = str(input_number)  # declare new variable which will convert integer to string
    string_to_list = []  # declare new variable which is list type
    for item in number_to_string:  # loop through each item in the string
        string_to_list.append(item)  # converted string to list data type using append function
    string_of_integers = ""  # declare new variable which is string type
    for item in string_to_list:  # loop through each item in the list
        item_square = int(item) ** 2  # declare new variable which will be square outcome as integer data type
        string_of_integers = string_of_integers + str(item_square)  # add square to already existing square
    output_number = int(string_of_integers)  # convert string to integer

    return output_number  # return output number


assert square_digits(9119) == 811181
assert square_digits(2483) == 416649
assert square_digits(3212) == 9414
