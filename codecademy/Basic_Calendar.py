"""
We’ll build a basic calendar that the user will be able to interact with from the command line. The user should be
able to choose to:
1. View the calendar. Done
2. Add an event to the calendar.
3. Update an existing event.
4. Delete an existing event.

The program should behave in the following way:
1. Print a welcome message to the user. Done
2. Prompt the user to view, add, update, or delete an event on the calendar.
3. Depending on the user’s input: view, add, update, or delete an event on the calendar.
4. The program should never terminate unless the user decides to exit.
"""
import calendar


class BasicCalendar:
    def __init__(self, welcome_message):
        self.welcome_message = welcome_message
        self.event = ""

    def view_calendar(self, year, month):
        text = calendar.TextCalendar()

        return text.formatmonth(year, month)

    def update_calendar(self, add_event):
        self.event = add_event

    def display_calendar(self):
        return self.event

    def delete_event(self,):
        self.event = ""


if __name__ == "__main__":
    basic_calendar_object = BasicCalendar("Welcome to my Calendar")
    print(basic_calendar_object.welcome_message)
    print(basic_calendar_object.view_calendar(2025, 10))
    basic_calendar_object.update_calendar("December 31")
    print(basic_calendar_object.display_calendar())
    basic_calendar_object.delete_event()
    print(basic_calendar_object.display_calendar())
