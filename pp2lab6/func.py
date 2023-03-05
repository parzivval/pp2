"""Write a Python program with builtin function to multiply all the numbers in a list"""
from operator import*
list=[1, 2, 3]
m = 1
for i in list:
	m = mul(i, m)
print(m)
"""Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters"""
str=str(input("Enter any sring: "))
l=0
u=0
for i in str:
  if(i.islower()):
    l+=1
  elif(i!=" "):
    u+=1
print("Lowercase characters: ",l)
print("Uppercase characters: ",u)
"""Write a Python program with builtin function that checks whether a passed string is palindrome or not"""
def isPal(str):
	rev=''.join(reversed(str))
	if (str==rev):
		return True
	return False
str=str(input("Enter any possible palindrome: "))
check=isPal(str)
if (check):
	print("Yes")
else:
	print("No")
"""Write a Python program that invoke square root function after specific milliseconds"""
from time import sleep
import math
def delay(sqr, ms, *n):
  sleep(ms/1000)
  return sqr(*n)
time=int(input("Enter time in ms: "))
number=int(input("Enter the number: "))
print("Square root of",number,"after",time,"miliseconds is",delay(lambda x: math.sqrt(x), time, number)) 
"""Write a Python program with builtin function that returns True if all elements of the tuple are true"""
n=input('Enter the number with spaces: ')
t=tuple(int(val) for val in n.split())
print(all(t))