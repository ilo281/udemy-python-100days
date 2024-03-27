def is_curzon(num):
    test = 2**num + 1
    test1 = 2*num + 1
    return_value = None
    if test % test1 == 0:
        return_value = True
    if test % test1 != 0:
        return_value = False
    if num < 0:
        return_value = "negative integer"

    return return_value


print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
print(is_curzon(-14))
