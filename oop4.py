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

class Cashier(Chef):
    raise_amt = 1.10

    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay)
        self.lang = lang

class Manager(Chef):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.first)



    
cash1 = Cashier('Squidvard','tentacles',1000,'Japanese')
cash2 = Cashier('Spinge','Bob',1000,'English')

#print(cash1.__dict__)
#print(help(Cashier))
# Method Resolution order
'''
when use super().__init__:
Python first looks at Cashier.
If it doesn't find it. It looks up the inheritance chain.
Cashier -> Chef -> builtins.object
Method resolution order:
 |      Cashier
 |      Chef
 |      builtins.object
 
'''
mgr1 = Manager('Elon','Mask',100,[cash1])
print(mgr1.employees)
mgr1.add(cash2)
print(mgr1.employees)
mgr1.print_emp()
mgr1.remove(cash1)
print(mgr1.employees)
mgr1.print_emp()
