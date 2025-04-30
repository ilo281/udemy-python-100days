# 1 Write a function that returns the number of users in a chatroom based on  rules:
def chatroom_status(list_with_users):
    number_users = ""
    l_minus_two = len(list_with_users) - 2
    l_minus_two_string = str(l_minus_two)
    if len(list_with_users) == 0:
        number_users = "no one online"
    if len(list_with_users) == 1:
        number_users = str(list_with_users[0]) + " online"
    if len(list_with_users) == 2:
        number_users = str(list_with_users[0]) + " and " + str(list_with_users[1]) + " online"
    if len(list_with_users) > 2:
        number_users = (str(list_with_users[0]) + ", " + str(list_with_users[1]) + " and " + l_minus_two_string
                        + " more online")

    return number_users


print(chatroom_status([]))
print(chatroom_status(["paRIE_to"]))
print(chatroom_status(["s234f", "mailbox2"]))
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833"]))
