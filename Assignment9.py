#Question 1
import time
import threading
from threading import Thread

def sleep():
     time.sleep(5)
     print("Thread woke up after 5 sec")
t=Thread(target=sleep,args=())
t.start()


# Question 2
import time
import threading
from threading import Thread

def sleep(x):
     print(x)
     time.sleep(1)
for x in range(11):
    t=Thread(target=sleep,args=(x,))
    t.start()


# Question 3
import time
import threading
from threading import Thread
def thread_process(i , b):
	    time.sleep(b)
	    print("Thread %i." % (i))

list = [1,2,3,4,5]
b=2
for i in list:
     t=Thread(target=thread_process,args=(i,b,))
     t.start()
     b+= 2


#Question 4
import time
import threading
from threading import Thread

def factorial(n):
    if n == 1:
        return 1
    else:
        f = n * factorial(n - 1)
        return f
        print("The factorial is:",f)
n = int(input("Enter the number"))
t=Thread(target=factorial,args=(n,))
t.start()

*** END****
