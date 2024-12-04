# 1 create a fuction that reverses a boolean
# 2 return the string "boolean expected" if another variable type is given
def reverse(input_value):
    return_value = None  # Initiate return_value with nothing
    if input_value:  # Check if input_value is true
        return_value = False
    if not input_value:  # Check if input_value is false
        return_value = True
    if type(input_value) is not bool:  # check if input_value is not boolean
        return_value = "boolean expected"

    return return_value


print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))
print(reverse("Mike"))

