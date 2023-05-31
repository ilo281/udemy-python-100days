import random

names_string = input("Give me everybody's names , separated by comma.")

names = names_string.split(",")

#print((names))

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_pay = names[random_choice]

print(person_who_pay + "is going to buy the meal today!")

#print(random_choice)

# ["Angela","Ben","Jenny","Michael","Chloe"]
mylist = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
print(mylist)