# Create a function to convert a list of percentages to their decimal equivalents.
class ConvertToDecimalNotation:
    def convert_to_decimal(self, list_of_percentages):
        list_of_decimal_equivalents = []
        for per in list_of_percentages:
            per_without_percent = per[:-1] # remove last element
            per_int = float(per_without_percent) # convert string to float
            decimal_equivalent = per_int/100
            list_of_decimal_equivalents.append(decimal_equivalent) # append decimal equivalent.

        return list_of_decimal_equivalents


if __name__ == "__main__": # entry into the code
    obj = ConvertToDecimalNotation()


assert obj.convert_to_decimal(["1%", "2%", "3%"]) == [0.01, 0.02, 0.03]
assert obj.convert_to_decimal(["45%", "32%", "97%", "33%"]) == [0.45, 0.32, 0.97, 0.33]
assert obj.convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) == [0.33, 0.981, 0.5644, 1]
