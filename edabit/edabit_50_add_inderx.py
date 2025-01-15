#1 create function which returns list of elements
#2 add index of each element to each element
def add_indexes(input_list):
    output_list = []
    for element in input_list:
        this_index = input_list.index(element)
        output_list.append(element + this_index)

    return output_list


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))
