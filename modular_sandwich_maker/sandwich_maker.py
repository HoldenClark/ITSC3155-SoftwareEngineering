### Complete functions ###
from Data import resources
from Data import recipes


def check_resources(self, size):
    self.size = size
    self.ingredients = recipes
    """Returns True when order can be made, False if current resources in machine are less than what would be required to make the sandwich."""
    if self.machine_resources['bread'] < self.machine_recipes[size]['ingredients']['bread'] or self.machine_resources[
        'ham'] < self.machine_recipes[size]['ingredients']['ham'] or self.machine_resources['cheese'] < \
            self.machine_recipes[size]['ingredients']['cheese']:
        return False
    else:
        return True


def make_sandwich(self, sandwich_size):
    self.sandwich_size = sandwich_size
    self.machine_recipes = recipes
    """The amount of each resource is subtracted by the amount that was made to make the sandwich."""
    self.machine_resources['bread'] = self.machine_resources['bread'] - \
                                      self.machine_recipes[sandwich_size]['ingredients']['bread']
    self.machine_resources['ham'] = self.machine_resources['ham'] - \
                                    self.machine_recipes[sandwich_size]['ingredients']['ham']
    self.machine_resources['cheese'] = self.machine_resources['cheese'] - \
                                       self.machine_recipes[sandwich_size]['ingredients']['cheese']
    print(f"{sandwich_size} sandwich is ready. Bon appetit!")
