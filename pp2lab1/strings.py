a = '''Avada
Kedavra'''
print(a)

a = "hello, world!"
print(a[0])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
price = 49.95
itemno = 567
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))