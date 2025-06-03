from coffee_machine import CoffeeMachine

machine = CoffeeMachine()
running = True

while running:
    options = machine.get_menu_display()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        print("Turning off. Goodbye!")
        running = False
    elif choice == "report":
        machine.report()
    elif choice in machine.menu:
        drink = machine.menu[choice]
        if machine.is_resource_sufficient(drink["ingredients"]):
            payment = machine.process_coins()
            if machine.complete_transaction(payment, drink["cost"]):
                machine.make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please select a valid drink.")
