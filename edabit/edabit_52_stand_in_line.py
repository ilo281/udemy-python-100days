# 1 write a function which takes a list and a number as argument
# 2 add the number to the end of the list
# 3 Remove the first element of the list
# 4 Return the updated list .
# 5 For an empty list input return " No list has been selected "
def next_in_line(input_list, input_number):
    if not input_list:
        output_list = "No list has been selected"
    else:
        output_list = input_list
        output_list.append(input_number)
        del (output_list[0])

    return output_list


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))

