#Question 1
list = (input('Enter the limit of  list: '))
print(list)

#Question 2
list = ["google","microsoft","tesla","facebook","apple"]
print(list)

#Question 3
aList = [123, 'xyz', 'def', 'abc', 123];
print("Count for 123 : ", aList.count(123))
print("Count for arr : ", aList.count('arr'))

#Question 4
num = [5, 12, 13, 14, 3, 54, 90]
print("Before sort list:", num)
num.sort()
print("After sort in ascending order list:", num)

#Question 5
A = [25, 18, 9, 41, 26, 31]
B = [25, 45, 3, 32, 15, 20]
C = A + B
C.sort()
print(C)

#Question 6
#Stack
color =["Red", "Blue", "Green", "Black"]
print(color)
color.append("White")
color.append("Yellow")
print(color)
color.pop()
color.pop()
color.pop()
print(color)

#Queue
color = ["Red", "Blue", "Green", "Black"]
color.append("White")
color.append("Yellow")
print(color)
color.popleft()
print(color)
color.popleft()
print(color)
color.popleft()
print(color)


#Question 7 #optional
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0
for x in numbers:
        if not x % 2:
    	     even+=1
        else:
    	     odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)