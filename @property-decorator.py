"""


The @property is a built-in decorator for the property() function in Python. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class


A decorator function is basically a function that adds new functionality to a function that is passed as argument. Using a decorator function is like adding chocolate sprinkles to an ice cream ?. It lets us add new functionality to an existing function without modifying it.

In the example below, you can see what a typical decorator function looks like in Python:

def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()
    return new_function

@decorator
def initial_function():
    print("Initial Functionality")

initial_function()


"""


class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

#>>> house = House(50000.0)  # Create instance
# >>> house.price = 45000.0   # Update value
# >>> house.price             # Access value
#45000.0
# >>> house = House(50000.0)
# >>> house.price = -50
# Please enter a valid price
# >>> house.price
# 50000.0

house = House(50000.0) # Create instance
house.price            # Access value 50000.0