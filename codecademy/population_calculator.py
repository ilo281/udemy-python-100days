
#Now, write a sentence that explains the change in population from 1927 to 2017, making use of your variables and string
#interpolation. Be sure to include the variables for the 1927 and 2017 population data, the change of population, and the
#annual growth rate of population. If you want to challenge yourself, you can also include the results of the rate of
#change between 1950 and 2000. Also feel free to find your own dataset!
#Save the sentence to a variable called report and print the sentence to the terminal#

city_name = "Istanbul, Turkey"

pop_1927 = 691000

pop_2017 = 15029231

pop_change = pop_2017 - pop_1927

percentage_gr = ((pop_2017 - pop_1927)/pop_1927) * 100

annual_gr = percentage_gr / 90

print(percentage_gr)


def population_growth(year_one, year_two, population_one, population_two):
    growth_rate = ((population_one - population_two)/population_two) * 100
    return growth_rate


print(population_growth(2017, 1927, 15029231, 619100))

print((f"Population of {city_name} in {1927} was {pop_1927} and in {2017} was {pop_2017}."))

print((f"Percentange growth for the entire period was {int(percentage_gr)} and annual growth was {int(annual_gr)}."))
