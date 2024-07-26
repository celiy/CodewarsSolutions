#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    newlist = []
    for p in lst:
        if p > 0:
            newlist.append(p)
    for p in lst:
        if p == 0:
            newlist.append(p)
    return newlist