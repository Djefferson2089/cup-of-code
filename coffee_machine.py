MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

class CoffeeMachine:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}
        self.profit = 0.0
        self.menu = MENU

    def report(self):
        """Print current resources and profit."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources.get('milk', 0)}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit:.2f}")

    def is_resource_sufficient(self, ingredients):
        """Check if enough resources to make drink."""
        for item in ingredients:
            if ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Get coin input and return total."""
        print("Please insert coins.")
        total = (
            int(input("How many quarters? ")) * 0.25 +
            int(input("How many dimes? ")) * 0.10 +
            int(input("How many nickels? ")) * 0.05 +
            int(input("How many pennies? ")) * 0.01
        )
        return round(total, 2)

    def complete_transaction(self, payment, cost):
        """Verify payment and handle change/profit."""
        if payment < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        if payment > cost:
            change = round(payment - cost, 2)
            print(f"Here is ${change} in change.")
        self.profit += cost
        return True

    def make_coffee(self, drink_name, ingredients):
        """Deduct ingredients and serve the drink."""
        for item in ingredients:
            self.resources[item] -= ingredients[item]
        print(f"Here is your {drink_name}. Enjoy!")

    def get_menu_display(self):
        """Return string of menu items with prices."""
        return " / ".join([f"{item} ${self.menu[item]['cost']}" for item in self.menu])
