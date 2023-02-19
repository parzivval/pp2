""" def gen(N):
    for i in range(N):
        yield i**2
g=gen(int(input('Enter a number: ')))
print(next(g)) """

""" def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
list=[]
for i in even(n):
    list.append(str(i))
print(",".join(list)) """

""" def threeandfour(n):
    i=0
    while i<=n:
        if i%3==0 and i%4==0:
            yield i
        i+=1
n=int(input())
list=[]
for i in threeandfour(n):
    list.append(str(i))
print(",".join(list)) """

""" def squares(a,b):
    while a<=b:
        yield a*a
        a+=1
a=int(input('Enter start number: '))
b=int(input('Enter end number: '))
for i in squares(a,b):
    print(i) """

def down(n):
    while n>=0:
        yield n
        n-=1
a=int(input('Enter start number: '))
for i in down(a):
    print(i)