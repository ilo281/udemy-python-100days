def find_odd(lst):
    lst_set = set(lst)
    odd_number = 0
    for number in lst_set:
        counter = lst.count(number)
        if counter % 2 == 0:
            pass
        else:
            odd_number = number

    return odd_number

    # 1 find integer which appears odd number of time
    # home work . comment what each line does .



print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))
