#There is an array with some numbers. All numbers are equal except for one. Try to find it!

#find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
#find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
#It’s guaranteed that array contains at least 3 numbers.

#The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    t = arr[0]
    if t != arr[1] and t!= arr[2]:
        return t
    for n, p in enumerate(arr):
        if t != p:
            if n <= len(arr):
                if arr[n-1] != p:
                    return p
                else:
                    return t