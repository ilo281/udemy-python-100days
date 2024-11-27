#1 Find elements of one type
#2 Move them to the end of list
def move_to_end(list_in, type_to_find):
    list_to_return = []
    for item in list_in:
        if item == type_to_find:
            list_in.append(list_in.pop(list_in.index(type_to_find)))

    return list_in


print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))
