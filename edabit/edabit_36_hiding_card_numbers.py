def card_hide(card):
    # create a list from numbers
    # loop though the list
    # return a string which display only four last numbers . Numbers before four last numbers need to be replaced with *

    card_numbers = list(card)
    card_numbers_length = len(card_numbers)

    characters_to_replace = card_numbers_length - 4

    counter = 0
    while counter < characters_to_replace:
        card_numbers[counter] = "*"
        counter = counter + 1

    output_card_number_length = len(card_numbers)
    if card_numbers_length == output_card_number_length:
        print("the length is the same ")
    string_to_return = "".join(card_numbers)
    return string_to_return


print(card_hide("1234123456785678"))
print(card_hide("8754456321113213"))
print(card_hide("35123413355523"))


