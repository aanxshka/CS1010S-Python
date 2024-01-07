def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i 
    return len(seq)
    """ Takes in a value x and a sorted sequence seq, and returns the first
    position that x should go to such that it will be less than or equal to
    the next element in the list. """
    return

def binary_search(x, seq):
    def helper(low,high):
        if low > high:
            return len(seq)
        mid = (low+high)//2
        if x > seq[mid-1] and x <= seq[mid]:
            return mid
        elif x < seq[mid]:
            return helper(low, mid-1)
        else:
            return helper(mid+1,high)
    
    if len(seq) == 0 or x <= seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        return helper(0,len(seq))
    
    """ Takes in a value x and a sorted sequence seq, and returns the first
    position that x should go to such that it will be less than or equal to
    the next element in the list. Uses O(lg n) time complexity algorithm. """


def insert_list(x, lst):
    y = search(x,lst)
    lst.insert(y,x)
    return lst
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""


def insert_tup(x, tup):
    y = search(x,tup)
    if x == 0:
        return (x,) + tup
    elif x == len(tup):
        return tup + (x,)
    else:
        return tup[:y] + (x,) + tup[y:]
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element and returns the resulting tuple."""

def sort_list(lst):
    sort = []
    for i in lst:
        sort = insert_list(i,sort)
    return sort

def sort_tup(tup):
    sort = ()
    for i in tup:
        sort = insert_tup(i,sort)
    return sort


def insert_animate(block_pos, shelf, high):
    i = 1 
    x = shelf[block_pos].size
    shelf.pop(block_pos)
    def search(x,shelf):
        for i in range(1,high):
            a = shelf[i-1].size
            b = shelf[i].size
            if x > a and x <= b:
                return i 
    
    if high == 1 or x < shelf[0].size:
        shelf.insert(0,x)
    else: 
        shelf.insert(search(x,shelf),x)
    """
    Pops the block at block_pos and inserts it in the position in the shelf
    such that its size is less than or equal to the one succeeding it. It searches
    for this position within zero and high.
    """
    # optional to return shelf but we do this for debugging 
    return shelf

def sort_me_animate(shelf):
    sort = []
    for i in range(0,len(shelf)):
        sort = insert_animate(i,shelf,i)
        
    return sort 
    """
    # optional to return shelf but we do this for debugging
    return shelf
    """
