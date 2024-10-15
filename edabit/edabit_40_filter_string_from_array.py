def filter_list(input_lst):
    # 1 filter out strings
    new_lst = []  # created new variable new_list
    for item in input_lst:  # loops through input_lst
        if type(item) is int:  # determine type of item
            new_lst.append(item)  # adds item to new_lst in case if item is integer

    return new_lst     # 2 return list without strings


print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
