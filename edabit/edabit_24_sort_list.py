def asc_des_none(lst, s):
    new_list = []
    if s == "None":
        new_list = lst
    if s == "Asc":
        lst.sort()
        new_list = lst
    if s == "Des":
        lst.sort(reverse=True)
        new_list = lst

    return new_list


print(asc_des_none([1, 2, 3, 4], "None"))
print(asc_des_none([4, 3, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
