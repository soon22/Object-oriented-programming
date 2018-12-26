'''
Class methods
Regular methods
Static methods
'''
import datetime

class Chef:

    num_of_chefs = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = int(pay)

        Chef.num_of_chefs +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    # Raise the raise_amt for the class
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    # Class method to enable parse a string (before __init__)then
    # create an instance
    @classmethod
    def from_string(cls, chefstr):
        first, last, pay = chefstr.split('-')
        return cls(first,last,pay)
    # Class method takes in class 'cls' as first argument
    # Regular method takes in instance 'self' as first argument
    # Static method takes none 
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

chef1 = Chef('Dongor','Ramsay',50)
chef2 = Chef('Jaime','Oliver', 100)
'''
print(Chef.raise_amt)
Chef.set_raise_amt(1.05)
print(Chef.raise_amt)
'''
#Chef.raise_amt = 100
print(Chef.raise_amt)
print(chef1.raise_amt)
print(chef2.raise_amt)

chef_str_1 = 'Johnny-English-100'

new_chef1 = Chef.from_string(chef_str_1)
print(new_chef1.__dict__)


my_date = datetime.date(2018,12,23)
print(Chef.is_workday(my_date))



















        
