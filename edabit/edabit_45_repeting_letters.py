# 1 create a function that take  a string and returns a string
def double_char(input_string):
# 2 returned string will need to have each characters from original string duplcated
    return_string = ""
    for character in input_string:
        return_string += character * 2
    return return_string


print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_ "))
