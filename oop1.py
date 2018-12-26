'''
Object oriented programming

class: consists of attributes and methods. A programming structure/ paradigm
        which allows  reuse of codes.
        to avoid typing same code again and again.
object: an instance of class
constructor: a method which is run automatically when an object is created.
            Kind of like mouse drivers that start automatically when you turn
            on the computer.

methods : like function
'''
class Fruit:
    #Constructor
    def __init__(self,name,color,taste):
        self.name = name
        self.color = color
        self.taste = taste
    # A method
    def describe(self):
        return '{} is {} in color and tastes {}'.format(
            self.name, self.color, self.taste)

# Instantiate an object of class Fruit
apple = Fruit('apple','green','sweet')
orange = Fruit('orange','blue','bitter')

print(apple)
print(apple.name)
print(apple.describe())

print(orange)
print(orange.name)
print(orange.describe())
