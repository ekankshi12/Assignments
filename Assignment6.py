#***  Question 1 ***
k = 0
while k<11 :
    name = input("Enter the name of friend : ")


# ***Question 2 ***
while True:
  print("Welcome to infinite loooop! ")

#*** Question 3 ***
a=[]
b=int(input("Enter value"))
for i in range(b):
    c=int(input())
    a.append(c)
for i in c:
    d = i**2
    print(d)

#*** Question 4 ***
myList = [ 4,'a',2.9, 'b', 'c',4.3, 1, 'd', 3, 66, 66.8, 'g']
types = set([type(item) for item in myList])
ret = {}
for typeT in set(types):
    ret[typeT] = [item for item in myList if type(item) == typeT]
print(ret)

# *** Question 5***
i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not (i%j):break
        j=j+1
    if(j>i/j): print(i,"is a prime number")
    i=i+1

# *** Question 6 ***
n = 0
print ("Pattern ")
for x in range (0,6):

    for a in range (0, n-1):
        print ('*', end = '')
    print()

# ***Question 7 ***
dictionary = {'parth': 16, 'ekankshi': 19 }
search_age = input("Enter age: ")
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print(name)

# ***Question 8***
a=[]
b=int(input("Enter value"))
for i in range(b):
    c=int(input())
    a.append(c)
print(a)
d = int(input("Enter element to search"))
if(d in a):
    a.remove(d)
else:
    print("Element not in list")

 #   ******END******