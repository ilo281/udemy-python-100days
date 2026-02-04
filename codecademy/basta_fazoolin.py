"""
1. Create a Menu class.

Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.

Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this
representation when the menu is available.
Try out our string representation. If you call print(brunch) it should print out something like the following:
brunch menu available from 11am to 4pm

Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of
purchased items.
Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.

Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries,
and one coffee. Pass that into brunch.calculate_bill() and print out the price.

"""

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price = total_price + item
        return total_price



if __name__ == "__main__":
    brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                    'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
    menu_object = Menu("Brunch", brunch_items, "11am", "4pm")
    print(menu_object.items)
    print(menu_object.name)
    print(menu_object.calculate_bill([brunch_items["pancakes"], brunch_items["home fries"], brunch_items["coffee"]]))

