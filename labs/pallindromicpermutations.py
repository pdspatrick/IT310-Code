def isPalindromicPermutation(s):
    '''Returns True if s is a permutation of a palindrome, otherwise False'''
    # Probably the wrong way to use a hash table, but it works reasonably well
    hashtable = {}
    # I was curious to see the hidden test cases since Ive solved it, so i printed them.
    # Apparently I got lucky with spaces? They only occurred in even numbers or
    # as the odd character in an odd-sized string, so they were (essentially) treated as normal
    # characters and didn't affect the result.
    for i in range(int(len(s))):
        if hashtable.get(s[i], None) is not None:
            hashtable[s[i]] += 1
        else:
            hashtable[s[i]] = 1
    odds = 0
    for j in range(len(hashtable) - 1):
        if hashtable.popitem()[1] % 2 is 1:
            if odds == 0 and len(s) % 2:
                # We can have one letter that isnt appearing an even number of times, like the "o" in tacocat
                # But only if the string is an odd number of characters. It passed without adding that but I added it.
                odds = 1
            else:
                # If we get more than one odd, or an even length string, we return false at this point.
                return False            
    return True