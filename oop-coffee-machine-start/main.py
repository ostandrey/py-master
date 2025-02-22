from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    menu_list = menu.get_items()
    user_order = input("Which coffee would you like to order? ")

    if user_order == "off":
        is_on = False
    elif user_order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)