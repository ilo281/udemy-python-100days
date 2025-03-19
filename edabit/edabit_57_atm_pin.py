# 1 create a function that take a string
# 2 validate if a string 4 or 6 characters
# 3 validate if a each element  is integer
# 4 return True if PIN is valid
# 5 return False if string is empty

def is_valid_PIN(input_string):
    output_boolean = False
    if len(input_string) == 6 or len(input_string) == 4:
        for element in input_string:
            if element.isdigit():
                output_boolean = True

    return output_boolean


print(is_valid_PIN("1234"))
print(is_valid_PIN("123456"))
print(is_valid_PIN("a3456"))
print(is_valid_PIN("12345"))
print(is_valid_PIN(""))
