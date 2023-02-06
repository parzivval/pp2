print(10 > 9)
#returns True

class myclass():
  def __len__(self):
    return 1
myobj = myclass()
print(bool(myobj))

def myFunction() :
  return False
if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))