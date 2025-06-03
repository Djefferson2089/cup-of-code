# cup-of-code
A command-line coffee machine simulation built in Python. This program allows users to order drinks like espresso, latte, or cappuccino, while managing limited resources like water, milk, and coffee grounds. It includes realistic interactions such as inserting coins, checking for sufficient resources, calculating change, and tracking profit.

# Features:

    Interactive command-line interface

    Drink selection: espresso, latte, cappuccino

    Resource tracking and reporting

    Coin processing and transaction validation

    Change calculation with rounding

    Graceful shutdown with an “off” command

# Technologies:

    Python 3

    Simple CLI interface (no external libraries)

# Operation Instructions

Follow these steps to use the coffee machine simulation in your terminal:
1. Start the Program

Run the application from your terminal:

python main.py

2. Choose a Drink

When prompted, enter the name of the drink you want to order:

What would you like? (espresso $1.5 / latte $2.5 / cappuccino $3.0):

    Type espresso, latte, or cappuccino to order a drink.

    Type report to see the current resource levels and money collected.

    Type off to shut down the machine and end the program.

3. Insert Coins

If resources are sufficient, you’ll be asked to insert coins:

Please insert coins.
How many quarters? 
How many dimes? 
How many nickels? 
How many pennies? 

The machine will calculate the total amount and verify if it covers the cost of the selected drink.
4. Transaction Result

Depending on the money inserted:

    ✅ If enough money is provided:

        The machine will dispense your drink

        It will return any extra change

        It will deduct ingredients from the resource stock

        You’ll see a message like: Here is your latte. Enjoy!

    ❌ If not enough money is inserted:

        The machine will cancel the transaction

        You’ll see: Sorry, that's not enough money. Money refunded.

5. Repeat Orders

After each transaction or report, the machine will prompt you again for another drink — until you type off to exit.

