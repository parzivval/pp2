#1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
"""class upperinput(object):
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())
string = upperinput()
string.getString()
string.printString()
"""
#2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""class shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        return 0
class square(shape):
    def area(self):
        return self.length**2
side = square(int(input()))
print(side.area())
"""
#3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
"""class shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return 0
  class rectangle(shape):
    def area(self):
        return self.length*self.width
length=int(input())
width=int(input())
rectaria = rectangle(length, width)
print(rectaria.area())
""" 
#4. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""class baccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance      
    def deposit(self, depositn):
        self.balance = self.balance + depositn
        print('Balance is {}'.format(self.balance))
    def withdraw(self, withdrawn):
            if withdrawn>self.balance:
                print('You have only {}'.format(self.balance))
            else:
                self.balance = self.balance - withdrawn
                print('Balance is {}'.format(self.balance))
command=input('deposit or withdraw: ')
if command=="deposit":
    d=baccount(int(input('What amount of money: ')))
    d.deposit()
else:
    w=baccount(int(input('What amount of money: ')))
    w.withdraw()"""
#5. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
numbers = []
while True:
    n=input()
    if n=='':
        break
    elif (int(n)>1):
      numbers.append(int(n))
prime = list(filter(lambda x:all(x % y !=0 for y in range(2,x)),numbers))
print(prime)
