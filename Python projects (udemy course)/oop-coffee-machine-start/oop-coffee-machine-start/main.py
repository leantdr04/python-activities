from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_calculator = MoneyMachine()
drink_list = Menu()

machine_on = True

while machine_on:
    drink = input(f"What would you like? {Menu().get_items()}: ").lower()
    if drink == "off":
        machine_on = False
    elif drink == "report":
        coffee_machine.report()
        money_calculator.report()
    else:
        coffee = drink_list.find_drink(drink)
        print(f"Price of {drink} is ${coffee.cost}")
        if coffee_machine.is_resource_sufficient(coffee) is True:
            if money_calculator.make_payment(coffee.cost) is True:
                coffee_machine.make_coffee(coffee)

