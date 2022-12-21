# Write a program for selling tickets to IT-events.
# Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket's price;
# -the ability to print a ticket as a String.

class RegularTicket:
    def __init__(self):
        self.price = 100
        self.unique_number = "02341"
        self.type = "regular"

    def __getattr__(self, atr_name):
        return 'Check if your data is correct'


class AdvanceTicket(RegularTicket):
    def __init__(self):
        super().__init__()
        self.discounted_price = 0
        self.unique_number = "02342"
        self.type = "advance"

    def count_discounted_price(self):
        self.discounted_price = (self.price * 60) / 100


class StudentTicket(RegularTicket):
    def __init__(self):
        super().__init__()
        self.discounted_price = 0
        self.unique_number = "02343"
        self.type = "student"

    def count_discounted_price(self):
        self.discounted_price = (self.price * 50) / 100


class LateTicket(RegularTicket):
    def __init__(self):
        super().__init__()
        self.discounted_price = 0
        self.unique_number = "02344"
        self.type = "late"

    def count_discounted_price(self):
        self.discounted_price = (self.price * 10) / 100 + self.price


def print_information(tickets, attribute, value):
    for ticket in tickets.values():
        if getattr(ticket, attribute) == value:
            print("Your ticket:\n"
                  f"\tUnique_number: {ticket.unique_number}\n"
                  f"\tType: {ticket.type}")

            if callable(ticket.count_discounted_price):
                ticket.count_discounted_price()
                print("\tPrice: %.2f" % ticket.discounted_price)
            else:
                print("\tPrice: %.2f" % ticket.price)
            return


def check_value(option, type, arguments):
    while option not in arguments:
        option = input(f"Please, select {type} that exist: ")
    return option

def main():
    tickets = {"regular_ticket": RegularTicket(),
               "advance_ticket": AdvanceTicket(),
               "student_ticket": StudentTicket(),
               "late_ticket": LateTicket()}

    print("Welcome to our company!\n\n"
          "Select the desired operation and enter the corresponding number:\n"
          "1: Construct the ticket by number\n"
          "2: Find out the price of the ticket\n"
          "3: Get out your ticket\n"
          "4: Exit the program\n")

    option = input("Your choice: ")
    option = check_value(option, 'option', ["1", "2", "3", "4"])

    if option == "1":
        unique_number = input("Enter unique number of ticket:\n"
                              "\t02341 - regular ticket\n"
                              "\t02342 - advance ticket\n"
                              "\t02343 - student ticket\n"
                              "\t02344 - late ticket\n")

        unique_number = check_value(unique_number, 'number', ["02341", "02342", "02343", "02344"])
        print_information(tickets, "unique_number", unique_number)
    if option == "2":
        type = input("Enter type of ticket:\n"
                     "\tregular\n"
                     "\tadvance\n"
                     "\tstudent\n"
                     "\tlate\n")

        type = check_value(type, 'type', ["regular", "advance", "student", "late"])
        print_information(tickets, "type", type)
    if option == "3":
        unique_number = input("Enter unique number of ticket:\n"
                              "\t02341\n"
                              "\t02342\n"
                              "\t02343\n"
                              "\t02344\n")

        unique_number = check_value(unique_number, 'number', ["02341", "02342", "02343", "02344"])
        print_information(tickets, "unique_number", unique_number)
    if option == "4":
        print("See you late")
        return


if __name__ == "__main__":
    main()
