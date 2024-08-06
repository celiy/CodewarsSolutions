#Digital root is the recursive sum of all the digits in a number.

#Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    nstr = str(n)
    nlist = []
    for c in nstr:
        nlist.append(c)
    res=0
    while True:
        for n, p in enumerate(nlist):
            nlist[n] = int(nlist[n])
        for p in nlist:
            res += p
        nstr = str(res)
        if len(nstr) <= 1:
            break
        else:
            nlist.clear()
            for c in nstr:
                nlist.append(c)
            res=0
    return res
