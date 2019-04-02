import random
def dualSelectionSort(lst):
    size = len(lst)
    for i in range(0,size):
        for j in range(-(size-i),0):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
random.seed(4321)
lst = [random.randint(1,500) for _ in range(25)]
#print(lst)
def selectionSort(lst):
    #print("Selsort prior to sort: " + str(lst))
    for i in range(len(lst)-1):
        minPosition = i
        for j in range(i+1, len(lst)):
            if lst[minPosition] > lst[j]:
               minPosition = j    
        temp = lst[i]
        lst[i] = lst[minPosition]
        lst[minPosition] = temp
    #print("Selsort after sort:   " + str(lst))
    return lst

def dualSelectionSort(lst):
    for i in range(len(lst)//2+1):
        minPosition = i
        maxPosition = len(lst)-i-1
        for j in range(minPosition+1, len(lst)-i):
            if lst[minPosition] > lst[j]:
                minPosition = j
            if lst[minPosition] > lst[len(lst) - j]:
                minPosition = -(len(lst) - j)
            if lst[maxPosition] < lst[j]:
                maxPosition = j
            if lst[maxPosition] < lst[len(lst) - j]:
                maxPosition = -(len(lst) - j) 
        tempmin = lst[i]
        tempmax = lst[len(lst)-i-1]
        lst[i] = lst[minPosition]
        lst[minPosition] = tempmin
        lst[len(lst)-i-1] = lst[maxPosition]
        lst[maxPosition] = tempmax
    return lst
random.seed(4321)
verifyfrom = 0
verifyto = len(lst)-1
sorted = [random.randint(1,500) for _ in range(25)]
print(lst == sorted)
sorted.sort()
print(sorted)
dualSelectionSort(lst)
print(lst)
print(lst == sorted)


lst = [131, 29, 209, 409, 33, 484, 91, 329, 188, 59, 464, 346, 22, 438, 96, 301, 28, 250, 149, 211, 309, 119, 206, 337, 483]
lst2 = [131, 29, 209, 409, 33, 484, 91, 329, 188, 59, 464, 346, 22, 438, 96, 301, 28, 250, 149, 211, 309, 119, 206, 337, 483]
lst2.sort()
def dualSelectionSort(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        for k in range(i+1,j-1):
            if lst[i] > lst[k]:
                lst[k] , lst[i] = lst[i], lst[k]
            if lst[j] < lst[k]:
                lst[j], lst[k] = lst[k], lst[j]
        i = i+1
        j = j-1
    return lst
print(dualSelectionSort(lst))
print(lst == lst2)