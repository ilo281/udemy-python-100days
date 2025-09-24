#  write a function that returns a list
#  has all duplicate elements removed.
# Is sorted from least to greatest value.

def unique_sort(input_list):
    output_list = []
    list_to_set = set(input_list)
    output_list = list(list_to_set)
    return output_list


assert unique_sort([1, 2, 4, 3, 4]) == [1, 2, 3, 4]
assert unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) == [1, 2, 3, 4]
assert unique_sort([6, 7, 3, 2, 1]) == [1, 2, 3, 6, 7]
