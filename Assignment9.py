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
for x in range(10):
    t=Thread(target=sleep,args=(x))
    t.start()


# Question 3
import time
import threading
from threading import Thread

list = [1,2,3,4,5]
def thread_process():
    time.sleep(2)
    print(list)
t=Thread(target=thread_process,args=())
t.start()


#Question 4
import time
import threading
from threading import Thread

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
t=Thread(target=factorial,args=(n))
t.start()