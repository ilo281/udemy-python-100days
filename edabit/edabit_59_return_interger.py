#1 Write a function that takes a list of elements
#2 returns only the integers
def return_only_integer(input_list):
    output_lst_integer = []
    for item in input_list:
        if type(item) is int:
            output_lst_integer.append(item)

    return output_lst_integer


print(return_only_integer([9, 2, "space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String",  True,  3.3,  1]))
