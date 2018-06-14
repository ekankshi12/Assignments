# **** Question 1 ****

# Error is the ZeroDivisionError
a=3
try:
    a = 3
    if a < 4:
        a = a / (a - 3)
except ZeroDivisionError:
    print("Invalid division: dividion by zero")


# **** Question 2 ****

# Error is the Index Error.
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("List index out of range")


# **** Question 3 ****
# Output of the code is:
#An exception
#Traceback (most recent call last):
#  File "C:/Users/HP/Desktop/Assign/test.py", line 2, in <module>
#    raise NameError("Hi there")
#NameError: Hi there

# **** Question 4 ****
# Output of the code is:
#-1.0
#a/b result in 0


# **** Question 5 ****
## 1
import sys
try:
    print(sys.version)
    import gw_utility.Book
except ImportError as error:
    print("Module not found error")
## 2
try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")

## 3
try:
    l=[1,2,3,4,]
    print(l[8])
except IndexError:
    print("List index out of range")

# **** Question 6 ****
class Error(Exception):
    pass
class AgeTooSmallError(Error):
    pass
age = int(input("Enter a the age"))
try:
    if age>=18:
        print("appropriate age")
    elif age<18:
        raise AgeTooSmallError
    else:
        print("Invalid input")

except AgeTooSmallError:
        print("Error: Age entered is less tham 18")