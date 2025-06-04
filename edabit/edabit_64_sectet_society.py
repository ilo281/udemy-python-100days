def society_name(list_of_names):
    secret_society_name = []
    for n in list_of_names:
        secret_society_name.append(n[0])
        ordered_name = sorted(secret_society_name)
        string_return = "".join(ordered_name)

    return string_return


print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
