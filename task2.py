# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.


class Pizza:
    def __init__(self):
        self.basic_ingredients = ["dough", "mozzarella", "sauce"]

    def __getattr__(self, atr_name):
        return 'Something wrong...'

    def add_ingredients(self, foodstuffs=[]):
        self.ingredients = [*self.ingredients, *foodstuffs]


class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Margherita"
        self.ingredients = [*self.basic_ingredients, "tomatoes", "basil"]
        self.day_of_week = "monday"


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Hawaiian"
        self.ingredients = [*self.basic_ingredients, "chicken", "pineapple", "maize"]
        self.day_of_week = "tuesday"


class Peperroni(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Peperroni"
        self.ingredients = [*self.basic_ingredients, "peperroni"]
        self.day_of_week = "wednesday"


class Supreme(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Supreme"
        self.ingredients = [*self.basic_ingredients, "pepperoni", "onion", "mushrooms", "pepper", "olives"]
        self.day_of_week = "thursday"


class Chicago(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago"
        self.ingredients = [*self.basic_ingredients, "beef", "sausage", "mushrooms", "pepperoni", "onion"]
        self.day_of_week = "friday"


class Sicilian(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Sicilian"
        self.ingredients = [*self.basic_ingredients, "tomato", "onion", "anchovies", "herbs"]
        self.day_of_week = "saturday"


class Greek(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Greek"
        self.ingredients = [*self.basic_ingredients, "tomato", "oregano", "olives", "feta", "onion"]
        self.day_of_week = "sunday"


def check_value(option, type, arguments):
    if type == 'ingredient':
        extra = option.split(", ")
        all_in_args = all(ingredient in arguments for ingredient in extra)

        while not all_in_args:
            option = input(f"Please, select {type} that exist: ")
            extra = option.split(", ")
            all_in_args = all(ingredient in arguments for ingredient in extra)
    else:
        while option not in arguments:
            option = input(f"Please, select {type} that exist: ")
    return option


def main():
    pizzas = {"monday": Margherita(),
              "tuesday": Hawaiian(),
              "wednesday": Peperroni(),
              "thursday": Supreme(),
              "friday": Chicago(),
              "saturday": Sicilian(),
              "sunday": Greek()}

    print("Welcome to our pizzeria!\n"
          "We offer pizza-of-the-day for business lunch")

    day_of_week = input("Enter the day of the week: ")
    day_of_week = check_value(day_of_week, 'day of the week', ["monday", "tuesday", "wednesday", "thursday",
                                                               "friday", "saturday", "sunday"])

    pizza = pizzas[day_of_week]

    print(f"Pizza of the day is {pizza.name}.\n"
          f"Ingredients: {', '.join(pizza.ingredients)}")
    extra_ingredients = input("Do you want add extra ingredients such as cheese, onion, tomato, mushrooms, maize?\n"
                              "(enter 'not' if don't want or write products in this format: 'cheese, onion, ...')\n")
    extra_ingredients = check_value(extra_ingredients, 'ingredient', ["cheese", "onion", "tomato", "mushrooms", "maize",
                                                                      "not"])

    if extra_ingredients != "not":
        pizza.add_ingredients(extra_ingredients.split(', '))

    print("Thank you!\n"
          f"You order {pizza.name} with such ingredients: \n\t{', '.join(pizza.ingredients)}")


if __name__ == "__main__":
    main()
