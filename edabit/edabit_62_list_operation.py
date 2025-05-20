# create a function that takes three parameters where x - start of range , y - the end of range , n - divisor
# return an ordered list with numbers in the range that are divisible by the third parametr .

def list_operation(x, y, n):
    ordered_lst = []
    for number in range(x, y + 1):
        if number % n == 0:
            ordered_lst.append(number)

    return ordered_lst


print(list_operation(1, 10, 3))
print(list_operation(7, 9, 2))
print(list_operation(15, 20, 7))
