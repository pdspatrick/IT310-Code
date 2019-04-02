import random, time, math


# this determines how far we go
# Numbers generated will be this times 5
# Offset is the number to start with. Lowest should be 1
degree = 50000
# How many steps to compute with regard to size
# ie 500 degree, 0 offset, with 50 steps means list increased in size by 10 each time
steps = 2
# random seed used for generation of list
seed = 1234
iterations = 1
# Name of file to use as output. Will output in a CSV format
filename = "./sortedtimes.csv"
# END OF CONFIGURABLES
########################################################################
########################################################################
# Helpers to make code easier to read and fix
iterations = 1
def timeIt(command, iterations):
    # time.time() wasnt working reliably for what I wanted to do.
    start = time.perf_counter_ns()
    for z in range(iterations):
        exec(command)
    stop = time.perf_counter_ns()
    totaltime = (stop - start) / iterations
    return totaltime
#########################################################################
# YAY THE MEAT NOW

def selectionSort(lst):
    for i in range(len(lst)):
       minPosition = i
       for j in range(i+1, len(lst)):
           if lst[minPosition] > lst[j]:
               minPosition = j    
       temp = lst[i]
       lst[i] = lst[minPosition]
       lst[minPosition] = temp
    return lst

def bubbleSort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(0, l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
def dualSelectionSort(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        for k in range(i,j):
            if lst[i] > lst[k]:
                lst[k], lst[i] = lst[i], lst[k]
            if lst[j] < lst[k]:
                lst[j], lst[k] = lst[k], lst[j]
        i = i+1
        j = j-1
    return lst
def insertionSort(lst):
    for i in range(1, len(lst)):
        j = i-1
        nextind = lst[i]	
        while (lst[j] > nextind) and (j >= 0):
            lst[j+1] = lst[j]
            j=j-1
        lst[j+1] = nextind
    return lst

random.seed(seed)
sorttimes = open(filename, "a")
numbers = [random.randint(1,degree * 5) for _ in range(degree)]
numbers.sort()


for i in range(0, len(numbers), degree//steps):
    liststart = time.perf_counter_ns()
    activeSel = numbers[:i]
    activeBub = numbers[:i]
    activeIns = numbers[:i]
    activeDS = numbers[:i]
    liststop = time.perf_counter_ns()
    listtime = liststop - liststart
    selsorttime = timeIt('selectionSort(activeSel)', iterations)
    inssorttime = timeIt('insertionSort(activeIns)', iterations)
    bubblesorttime = timeIt('bubbleSort(activeBub)', iterations)
    dualslsorttime = timeIt('dualSelectionSort(activeDS)', iterations)
    #if activeSel == numbers[:i] or activeBub == numbers[:i] or activeIns == numbers[:i] or activeDS == numbers[:i]: 
        #print("List of size " + str(i) + " appears to already be sorted. Dropping!")
    if not activeSel == activeBub == activeIns == activeDS:
        print("Sorted Lists for length of " + str(i) + " did not match. Dropping!")
    else:
        sorttimes.write(str(i) + "," + str(selsorttime)  + "," + str(inssorttime)  + "," + str(bubblesorttime) + "," + str(dualslsorttime) + "\n")
    sorttimes.flush()
sorttimes.close()