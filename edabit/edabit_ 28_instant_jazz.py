def jazzify(input_list):
    list_to_return = []
    for letter in input_list:
        if "7" in letter:
            list_to_return.append(letter)
        if "7" not in letter:
            list_to_return.append(letter + "7")

    return list_to_return


print(jazzify(["G", "F", "C"]))
print(jazzify(["Dm", "G", "E", "A"]))
print(jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(jazzify([]))
