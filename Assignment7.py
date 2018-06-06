#   **Question 1**
#r =int(input("Enter the radius : "))

#def calc_area(r):
#    '''Docstring example'''
 #   PI = 3.14159
 #   area=PI*r**2
#    return area
#print("The area of the circle for entered radius is: ",calc_area(r))

# **Question 2**
#number = int(input(" Please Enter any Number: "))
#def perfect(number):
#    Sum = 0
#    for i in range(1, 1000):
#        if(number % i == 0):
#            Sum = Sum + i
#            return Sum
#    if (Sum == number):
#        print(" %d is a Perfect Number" %number)
#    else:
#        print(" %d is not a Perfect Number" %number)
#print("This is the function call: ",perfect(number))

# **Question 3**
#num = 12
#def table():
#    for i in range(1, 11):
#        print(num,'x',i,'=',num*i)
#table()

# **Question 4**
#def power_num(b,e):
#    if(e==1):
#        return(b)
#        return(b*power_num(b,e-1))
#b=int(input("Enter base: "))
#e=int(input("Enter exponential value: "))
#print("Result:",power_num(b,e))

# **Question 5**
#def factorial(n):
#    if(n <= 1):
#        return 1
#    else:
#        f = n * factorial(n - 1)
#        return(f)
#n = int(input("Enter number:"))
#print("Factorial:")
#print(factorial(n))
#dict ={}
#dict.update({n:factorial(n)})
#print(dict)