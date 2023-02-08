#1.A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def convertgrams(x):
	return 28.3495231*x
ounces = convertgrams(int(input('Enter grams: ')))
print(ounces)
#2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def convertT(f):
    return (5.0/9.0)*(f-32)
c=convertT(int(input('Enter a Fahrenheit temperature: ')))
print(c,"centigrade")
#3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def puzzle(heads,legs):
    for x in range(heads+1):
        y=heads-x
        if 2*x+4*y==legs:
            return x,y
heads=35
legs=94
solution=puzzle(heads,legs)
print (solution)
#4.You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.


def primef(numbers):
        return list(filter(lambda x: all(x % y !=0 for y in range(2,x)), numbers))
numbers = []
while True:
    n=input()
    if n=='':
        break
    elif (int(n)>1):
      numbers.append(int(n))
primenum=primef(numbers)
print(primenum)
#5.Write a function that accepts string from user and print all permutations of that string.
def output(list):
    return ''.join(list)
def permute(a, l, r):
    if l==r:
        print(output(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
string=str(input("Enter any word: "))
n=len(string)
a=list(string)
permute(a, 0, n-1)
#6.Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def revstr(text):
    string = text.split()
    string.reverse()
    newstring = ' '.join(string)
    return newstring
a=revstr(str(input()))
print(a)
#7.Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    #def has_33(nums):
        #pass

    #has_33([1, 3, 3]) → True
    #has_33([1, 3, 1, 3]) → False
    #has_33([3, 1, 3]) → False

def has33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
list = [4,0,3]
print(has33(list))
#8. Write a function that takes in a list of integers and returns True if it contains 007 in order
#def spy_game(nums):
    #pass

    #spy_game([1,2,4,0,0,7,5]) --> True
    #spy_game([1,0,2,4,0,5,7]) --> True
    #spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True
                else:
                    return False
a=spy_game([0,0,0,1])
print(a)
#9. Write a function that computes the volume of a sphere given its radius.
def volumeSphere(radius): 
   x = (4/3) * 3.142 
   y = radius ** 3 
   volume = x * y 
   return volume 
a=volumeSphere(9.0)
print(a)
#10.Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uniquelist(numbers):
  unique = []
  for n in numbers:
    if n not in unique:
      unique.append(n)
  return unique

print(uniquelist([1,1,2,3,4,5])) 
#11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def isPal(str):
    return str==str[::-1]
str=str(input())
isPalindrome = isPal(str)
print(isPalindrome)
#12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

#****
#*********
#*******
def histogram(list):
    for i in range(len(list)):
        print (list[i]*'*')
list = [4,9,7]
histogram(list)
#13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
    #Hello! What is your name?
    #KBTU

    #Well, KBTU, I am thinking of a number between 1 and 20.
    #Take a guess.
    #12

    #Your guess is too low.
    #Take a guess.
    #16

    #Your guess is too low.
    #Take a guess.
    #19

#14. Good job, KBTU! You guessed my number in 3 guesses!
#Create a python file and import some of the functions from the above 13 tasks and try to use them.