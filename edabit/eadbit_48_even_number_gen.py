# 1 create a function that finds all even numbers

def find_even_nums(last_number_of_range):
    output_list = []
    for number in range(1, last_number_of_range + 1):
        if number % 2 == 0:
            output_list.append(number)

    return output_list


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
