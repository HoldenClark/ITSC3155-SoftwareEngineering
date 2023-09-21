def process_coins(self, size):
    self.size = size
    """Returns the total calculated from coins inserted."""
    # total_price represents the amount of money is required to make the sandwich.
    total_price = float(self.machine_recipes[size]['cost'])

    # total price of sandwich is geven to customer and customer is asked to input money to pay for sandwich.
    print(f"Total price of the sandwich is ${total_price:.2f}. Please insert coins.")

    change = self.enter_coin_values(total_price)
    # if the amount placed in the machine is greater than or equal to the amount required then the sandwich will be made and change greater than or equal to $0.00 will be returned.
    if change >= 0.0:
        self.money_in_machine += total_price
        print(f"Transaction completed, your change is: ${change:.2f}")
        return True
    else:
        print("Not enough money was entered into the machine. Transaction refunded.")
        return False


def enter_coin_values(self, total_price):
    self.total_price = total_price
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
