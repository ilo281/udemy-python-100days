def relation_to_luke(name):
    relation = ""
    if name == "Darth Vader":
        relation = "Luke, I am your father"
    if name == "Leia":
        relation = "Luke, I am your sister"
    if name == "Han":
        relation = "Luke, I am your brother in law"

    return relation


print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
