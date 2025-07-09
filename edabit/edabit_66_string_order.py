# Create a function that takes a string and returns True or False,
# If characters in order return  True if not return False

class Order:
    def is_in_order(self, input_string):
        ordered_string = False
        sorted_input_string = sorted(input_string)
        input_string_as_list = []
        for i in input_string:
            input_string_as_list.append(i) # append function convert string to list
        if input_string_as_list == sorted_input_string:
            ordered_string = True

        return ordered_string
    def mike(self):
        return "steve."


order_object = Order() # creating instance of a class
assert order_object.mike() == "steve." # assertions are units tests
assert order_object.is_in_order("abc")
assert not order_object.is_in_order("edabit") # not is meaning not equal to
assert order_object.is_in_order("123")
assert order_object.is_in_order("xyzz")
