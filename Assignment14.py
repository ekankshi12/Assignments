# *** Question 1 ***
def LastNLines(f,n):
    with open(f) as file:
        print('last', n, 'lines from file:', f)
        for line in (file.readlines() [-n:]):
            print(line,end='')

name = input("Enter the file name")
n = int(input('No. of last lines to read:'))
try:
    LastNLines(name,n)
except:
    print('File Error..')


# *** Question 2 ***
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("demo.txt"))


# *** Question 3 ***
with open("demo.txt") as f:
    with open("test.txt", "w") as f1:
        for line in f:
            f1.write(line)


# *** Question 4 ***
with open('demo.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)


# *** Question 5 ***
import random
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res
num = 10
start = 1
end = 40
print(Rand(start, end, num))