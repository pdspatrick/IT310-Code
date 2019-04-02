lst = [131, 29, 209, 409, 33, 484, 91, 329, 188, 59, 464, 346, 22, 438, 96, 301, 28, 250, 149, 211, 309, 119, 206, 337, 483]
lst2 = [131, 29, 209, 409, 33, 484, 91, 329, 188, 59, 464, 346, 22, 438, 96, 301, 28, 250, 149, 211, 309, 119, 206, 337, 483]
lst2.sort()
def dualSelectionSort(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        for k in range(i,j):
            if lst[i] > lst[k]:
                print("Swapping i and k")
                lst[k], lst[i] = lst[i], lst[k]
            if lst[j] < lst[k]:
                print("Swapping j and k")
                lst[j], lst[k] = lst[k], lst[j]
        i = i+1
        j = j-1
    return lst
print(dualSelectionSort(lst))
print(lst == lst2)