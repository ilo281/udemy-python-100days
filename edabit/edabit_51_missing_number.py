# create a function which take list of numbers between 1 and 10 ,excluding one number
# find and return a missing number

def missing_num(input_list):
    output_number = 0
    good_list = list(range(1, 11))
    sorted_input_list = sorted(input_list)
    set1 = set(sorted_input_list)
    set2 = set(good_list)
    list_out = list(sorted(set2 - set1))
    output_number = list_out[0]

    return output_number


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))

