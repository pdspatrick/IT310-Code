import time, math, random

# this determines how far we go
degree = 500
steps = 50
# runs to do and get an average
# prefix3 does 10 times this number
numberofruns = 1

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = int(0)
        for i in range(j+1):
            total += S[i]
        A[j] = total // (j+1)
    return A

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) // (j+1)
    return A

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total // (j+1)
    return A

prefixout = open("prefix.csv", "a")


random.seed(1234)
numbers = [random.random() for _ in range(degree)]
numberofruns10 = numberofruns * 10
for i in range(10000000, len(numbers), degree//steps):
    active = numbers[:i]
    print(i)
    prefix1start = time.time()
    for f in range(numberofruns):
        prefix_average1(active)
    prefix1end = time.time()
    prefix2start = time.time()
    for f in range(numberofruns):
        prefix_average2(active)
    prefix2end = time.time()
    prefix3start = time.time()
    for f in range(numberofruns10):
        prefix_average3(active)
    prefix3end = time.time()
    prefix1time = (prefix1end - prefix1start) / numberofruns
    prefix2time = (prefix2end - prefix2start) / numberofruns
    prefix3time = (prefix3end - prefix3start) / (numberofruns /10 )
    prefixout.write(str(i) + "," + str(prefix1time)  + "," + str(prefix2time)  + "," + str(prefix3time) + "\n")
    prefixout.flush()
prefixout.close()