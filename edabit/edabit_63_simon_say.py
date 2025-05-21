# 1 create a function that  takes in two lists and returns True if second
# 2 second list follows the first list by one element ,and False otherwise
def simon_says(list_1, list_2):
    result = None
    for number_in_list_1 in list_1:
        for number_in_list_2 in list_2:
            if number_in_list_1 - number_in_list_2 == 1:
                result = True
            else:
                result = False
    return result


print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
