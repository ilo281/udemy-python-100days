# Create a function that takes a string and returns either True or False
# If this string is  "isogram" return True if not return False
def is_isogram(input_string):
    output = True
    input_string_lower = input_string.lower()

    for letter in input_string_lower:
        duplicate = input_string_lower.count(letter)
        if duplicate == 2:
            output = False

    return output


print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))
