def XO(input_string):
    # count number of x
    input_string_lower = input_string.lower()
    boolean = 0
    count_x = input_string_lower.count("x")
    # count number of o
    count_o = input_string_lower.count("o")

    # check if string has same number o and x
    # return True if x and o are the same amount
    # return False if not the same amount
    # When x and o not in the string return True
    if count_x == count_o:
        boolean = True
    if count_x != count_o:
        boolean = False
    if "x" not in input_string_lower and "o" not in input_string_lower:
        boolean = True

    return boolean


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("zpzpzpp"))
print(XO("ooxXm"))
print(XO("zzoo"))
