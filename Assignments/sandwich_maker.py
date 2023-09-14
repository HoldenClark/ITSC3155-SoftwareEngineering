### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources, machine_recipes):
        """Resources are assigned to machine so the object knows how much of each item is available.
        Recipes are assigned to machine so the object knows how much of each item to use for each sandwich.
        Total money in machine is set to 0 and incremented everytime a sandwich is sold by the value of the sandwich."""
        self.machine_resources = machine_resources
        self.machine_recipes = machine_recipes
        self.money_in_machine = 0

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if current resources in machine are less than what would be required to make the sandwich."""
        if self.machine_resources['bread'] < self.machine_recipes[ingredients]['ingredients']['bread'] or self.machine_resources['ham'] < self.machine_recipes[ingredients]['ingredients']['ham'] or self.machine_resources['cheese'] < self.machine_recipes[ingredients]['ingredients']['cheese']:
            return False
        else:
            return True

    def process_coins(self, size):
        """Returns the total calculated from coins inserted."""
        #total_price represents the amount of money is required to make the sandwich.
        total_price = float(self.machine_recipes[size]['cost'])

        #total price of sandwich is geven to customer and customer is asked to input money to pay for sandwich.
        print(f"Total price of the sandwich is ${total_price:.2f}. Please insert coins.")

        change = self.enter_coin_values(total_price)
        #if the amount placed in the machine is greater than or equal to the amount required then the sandwich will be made and change greater than or equal to $0.00 will be returned.
        if change >= 0.0:
            self.money_in_machine += total_price
            print(f"Transaction completed, your change is: ${change:.2f}")
            return True
        else:
            print("Not enough money was entered into the machine. Transaction refunded.")
            return False

    def make_sandwich(self, sandwich_size):
        """The amount of each resource is subtracted by the amount that was made to make the sandwich."""
        self.machine_resources['bread'] = self.machine_resources['bread'] - self.machine_recipes[sandwich_size]['ingredients']['bread']
        self.machine_resources['ham'] = self.machine_resources['ham'] - \
                                          self.machine_recipes[sandwich_size]['ingredients']['ham']
        self.machine_resources['cheese'] = self.machine_resources['cheese'] - \
                                          self.machine_recipes[sandwich_size]['ingredients']['cheese']
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    #calculates value of coins entered. uses total price of item and total amount entered to return to the user their change.
    def enter_coin_values(self, total_price):
        try:
            large_dollars = float(input("how many large dollars?: "))
            half_dollars = float(input("how many half dollars?: "))
            quarters = float(input("how many quarters?: "))
            nickels = float(input("how many nickels?: "))
            total_input = large_dollars + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
            change = float(total_input - total_price)
            return change
        except Exception as e:
            print(f"Please enter a integer value. Exception {e} was caught")
            change = self.enter_coin_values(total_price)
            return change

#instance of sandwichMachine class. size is set to value so while loop begins running.
sandwich_maker = SandwichMachine(resources, recipes)
size = 'not off'
while(size != 'off'):
    size = input("What would you like? (small/ medium/ large/ off/ report): ")
    #if 'off' is entered machine turns off and process is finished.
    if size == 'off':
        break

    # 'report' will return the amount of each resource left and the amount of money the machine has made.
    elif size == 'report':
        print(f"The machine currently has: {sandwich_maker.machine_resources['bread']} slices of bread, {sandwich_maker.machine_resources['ham']} slices of ham, {sandwich_maker.machine_resources['cheese']} slices of cheese and the machine contains ${sandwich_maker.money_in_machine:.2f}!")
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