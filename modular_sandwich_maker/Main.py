from sandwich_maker import make_sandwich
from sandwich_maker import check_resources
from cashier import process_coins
from cashier import enter_coin_values
from Data import resources
from Data import recipes


class SandwichMachine:

    def __init__(self):
        """Resources are assigned to machine so the object knows how much of each item is available.
        Recipes are assigned to machine so the object knows how much of each item to use for each sandwich.
        Total money in machine is set to 0 and incremented everytime a sandwich is sold by the value of the sandwich."""
        self.machine_resources = resources
        self.machine_recipes = recipes
        self.money_in_machine = 0

    def check_resources(self, size):
        return check_resources(self, size)

    def process_coins(self, size):
        return process_coins(self, size)

    def make_sandwich(self, size):
        return make_sandwich(self, size)

    def enter_coin_values(self, total_price):
        return enter_coin_values(self, total_price)

# instance of sandwichMachine class. size is set to value so while loop begins running.
sandwich_maker = SandwichMachine()
size = 'not off'
while size != 'off':
    size = input("What would you like? (small/ medium/ large/ off/ report): ")
    # if 'off' is entered machine turns off and process is finished.
    if size == 'off':
        break

    # 'report' will return the amount of each resource left and the amount of money the machine has made.
    elif size == 'report':
        print(
            f"The machine currently has: {sandwich_maker.machine_resources['bread']} slices of bread, {sandwich_maker.machine_resources['ham']} slices of ham, {sandwich_maker.machine_resources['cheese']} slices of cheese and the machine contains ${sandwich_maker.money_in_machine:.2f}!")
        continue

    # if it is possible to make the sandwich then functions are called to input money and deduct resources.
    elif size == 'small' or size == 'medium' or size == 'large':
        if sandwich_maker.check_resources(size):
            if sandwich_maker.process_coins(size):
                sandwich_maker.make_sandwich(size)
        else:
            print("Your sandwich could not be made, there are not enough resources left in the machine.")
    else:
        print("Please type the options correctly.")
