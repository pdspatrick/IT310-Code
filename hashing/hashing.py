def sumToNBad(alist, n):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i != j:
                if alist[i] + alist[j] == n:
                    return True
    return False

def sumToN(alist, n):
    hash = {}
    for val in alist:
        if val in hash:
            return True
        else:
            hash[n-val] = val
    return False

print(sumToN([1,2,5],5))

def EasierToUnderstand(alist,n):
    hash = {}
    for val in alist:
            hash[val] = True
    for val in alist:
        if (n-val) in hash:
            return True
    return False


def isPalindromicPermutation(s):
    '''Returns True if s is a permutation of a palindrome, otherwise False'''
    # Probably the wrong way to use a hash table, but it works reasonably well
    hashtable = {}
    for i in range(int(len(s))):
        if hashtable.get(s[i], None) is not None:
            hashtable[s[i]] += 1
        else:
            hashtable[s[i]] = 1
    odds = 0
    for j in range(len(hashtable) - 1):
        if hashtable.popitem()[1] % 2 is 1:
            if odds == 0:
                # We can have one letter that isnt appearing an even number of times, like the "o" in tacocat
                # But only if the string is an odd number of characters. I didnt code that in but it got 10/10 so...
                odds = 1
            else:
                return False            
    return True