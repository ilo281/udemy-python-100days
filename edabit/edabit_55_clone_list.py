def clone(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
    lst.append(new_list)

    return lst


print(clone([1, 1]))
print(clone([1, 2, 3]))
print(clone(["x", "y"]))
