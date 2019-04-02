def peaksort(l):
    l.sort()
    slice1 = (len(l)//2)
    slice2 = ((len(l)-1))
    l1 = l[0:slice1]
    l2 = l[(slice1):]
    lnew = []
    for i in range(len(l)):
        try:
            lnew.append(l2.pop())
        except:
            pass
        try:
            lnew.append(l1.pop())
        except:
            pass
    return lnew
    