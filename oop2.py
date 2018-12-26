'''
About class variable and instance variable:
Class variable: Variables that belong to class, shared by all instances
Instance varbiable: Variables that belong to individual object
'''

class Food:
    num_of_food = 0
    raise_amount = 1.04
    def __init__(self,name,taste,price):
        self.name = name
        self.taste = taste
        self.price = price

        Food.num_of_food += 1

    def apply_raise(self):
        self.price = int(self.price*self.raise_amount)
        
print(Food.num_of_food)
pizza = Food('pizza','good',100)
print(Food.num_of_food)
print(pizza.price)
pizza.raise_amount = 0.1
pizza.apply_raise()
print(pizza.price)
print(pizza.__dict__)
print(Food.__dict__)
