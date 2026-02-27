"""
2. Creating the Franchises

First, let’s create a Franchise class.

Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus
and assign it to self.menus.

Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment
is located at "12 East Mulberry Street". Pass in Branch menu along with these addresses to define flagship_store and
new_installment.

Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a Franchise it
should tell us the address of the restaurant.

Let’s tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time
parameter and returns a list of the Menu objects that are available at that time.

Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
"""

class Franchise:
    def __init__(self, address, list_menus):
        self.address = address
        self.list_menus = list_menus

    def available_menus(self,time):
        menus = ""
        if time == "7pm":
            menus = "dinner"
        if time == "10am":
            menus = "breakfast"


        return menus

if __name__ == "__main__":
    address = "1232 West end Road"
    brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                    'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

    flagship_store = Franchise(address, brunch_items)
    print(flagship_store.list_menus)
    print(flagship_store.address)
    time = "2pm"
    print(flagship_store.available_menus(time))

    new_installment_address = "12 East Mulberry Street"
    new_installment = Franchise(new_installment_address, brunch_items)
    print(new_installment.list_menus)
    print(new_installment.address)
    print(new_installment.available_menus("10am"))
