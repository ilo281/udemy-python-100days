# create a function  that takes a temperature input in celsius
# convert it to Fahrenheit
# Return the converted temperature

def temp_conversion(tmp_celsius):
    tmp_fahrenheit = tmp_celsius*9/5 + 32
    tmp_list_to_return = []
    tmp_list_to_return.append(tmp_fahrenheit)
    return tmp_list_to_return


print(temp_conversion(0))
print(temp_conversion(100))
print(temp_conversion(-10))
print(temp_conversion(300.4))
