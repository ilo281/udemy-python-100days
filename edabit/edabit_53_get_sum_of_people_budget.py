# 1 create a function that takes a list of dictionaries
# 2 calculate the sum of people budget
# 3 return the sum of people's budget.
def get_budgets(list_of_dictionaries):
    sum_of_budgets = 0

    for person in list_of_dictionaries:

        each_person_budget = person.get("budget")
        sum_of_budgets = sum_of_budgets + each_person_budget

    return sum_of_budgets


print(get_budgets(
    [{"name": "John", "age": 21, "budget": 23000}, {"name": "Steve", "age": 32, "budget": 40000},
     {"name": "Martin", "age": 16, "budget": 2700}]))  # ➞ 65700


print(get_budgets([
  {"name": "John",  "age": 21, "budget": 29000},
  {"name": "Steve",  "age": 32, "budget": 32000},
  {"name": "Martin",  "age": 16, "budget": 1600}]))

