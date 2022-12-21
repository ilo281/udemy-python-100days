# Brainstorming : )
# need to calculate 12 % from 150 .
# We do that dividing 12 /100 * 150


print("welcome to the tip calculator")

amount = float(input("What is total bill ? "))

tip = int(input("how much tip would you give  12 ,10 ? "))

people = int(input("how many people split the bill "))

tip_as_percent = tip / 100

total_tip_amount = amount*tip_as_percent

total_amount = amount+total_tip_amount

amount_per_person = total_amount / people

final_amount = round(amount_per_person, 2)

print(final_amount)





