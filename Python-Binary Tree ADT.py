###########
# Task 1a #
###########

def build_tree(entry, left, right):
    return [entry,left,right]
    


###########
# Task 1b #
###########

def entry(tree):
    return tree[0]
    

def left_branch(tree):
    # Your code here
    return tree[1]

def right_branch(tree):
    # Your code here
    return tree[2]


###########
# Task 1c #
###########

def make_empty_tree():
    # Your code here
    return []


###########
# Task 1d #
###########

def is_empty_tree(tree):
    if tree == []:# Your code here
        return True
    else:
        return False


###########
# Task 2a #
###########
def insert_tree(x, tree):
    if is_empty_tree(tree):
        return build_tree(x,make_empty_tree(),make_empty_tree())
    elif x <= entry(tree):
        return build_tree(entry(tree),insert_tree(x,left_branch(tree)), right_branch(tree))
    else:        
        return build_tree(entry(tree), left_branch(tree), insert_tree(x,right_branch(tree)))
    """
    - tree is empty -> return a tree with x as entry and empty left and right branches
    - x <= entry -> return new tree with x inserted into left sub tree
    - otherwise -> return new tree with x inserted into right sub tree
    """
    # Your code here
    
###########
# Task 2b #
###########
# Time complexity of insert_tree: O(n) where n is max number of levels of the tree
# Explanation: There is a total of n recurive calls. 
###########
# Task 2c #
###########
def contains(x, tree):
    
    if is_empty_tree(tree):
        return False
    elif x == entry(tree):
        return True
    elif x <= entry(tree):
        return contains(x,left_branch(tree))
    elif x > entry(tree):
        return contains(x,right_branch(tree))
    
    """ Returns true if x is in binary tree, otherwise return false """
    # Your code here
###########
# Task 2d #
###########
# Time complexity of insert_tree: O(n) where n is max number of levels of the tree
# Explanation: There is a total of n recurive calls. 
###########
# Task 2e #
###########
def flatten(tree):
    if is_empty_tree(tree):
        return []
    else:
        return flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree))
    """ flattens tree with the following rule:
        visit left branch, visit entry then visit right branch """
    # Your code here
###########
# Task 2f #
###########
# Time complexity of flatten:O(2**n) where n is max number of levels of the tree.
# Explanation: There aer two recursive calls to flatten(tree) resulting in a tree recursion with branching factor of 2 
###########
# Task 2a #
###########
def insert_tree(x, tree):
    if is_empty_tree(tree):
        return build_tree(x,make_empty_tree(),make_empty_tree())
    elif x <= entry(tree):
        return build_tree(entry(tree),insert_tree(x,left_branch(tree)), right_branch(tree))
    else:        
        return build_tree(entry(tree), left_branch(tree), insert_tree(x,right_branch(tree)))
    """
    - tree is empty -> return a tree with x as entry and empty left and right branches
    - x <= entry -> return new tree with x inserted into left sub tree
    - otherwise -> return new tree with x inserted into right sub tree
    """
    # Your code here
    
###########
# Task 2b #
###########
# Time complexity of insert_tree: O(n) where n is max number of levels of the tree
# Explanation: There is a total of n recurive calls. 
###########
# Task 2c #
###########
def contains(x, tree):
    
    if is_empty_tree(tree):
        return False
    elif x == entry(tree):
        return True
    elif x <= entry(tree):
        return contains(x,left_branch(tree))
    elif x > entry(tree):
        return contains(x,right_branch(tree))
    
    """ Returns true if x is in binary tree, otherwise return false """
    # Your code here
###########
# Task 2d #
###########
# Time complexity of insert_tree: O(n) where n is max number of levels of the tree
# Explanation: There is a total of n recurive calls. 
###########
# Task 2e #
###########
def flatten(tree):
    if is_empty_tree(tree):
        return []
    else:
        return flatten(left_branch(tree)) + [entry(tree)] + flatten(right_branch(tree))
    """ flattens tree with the following rule:
        visit left branch, visit entry then visit right branch """
    # Your code here
###########
# Task 2f #
###########
# Time complexity of flatten:O(2**n) where n is max number of levels of the tree.
# Explanation: There aer two recursive calls to flatten(tree) resulting in a tree recursion with branching factor of 2 


###########
# Task 3a #
###########
def sort_it(lst):
    tree = make_empty_tree()
    for i in lst:
        tree = insert_tree(i,tree)
    sort = flatten(tree)
    # Your code here
    return sort
###########
# Task 3b #
###########
# Time complexity of sort_it: O(n**2x2**n) where n is the max levels of the tree
# Explanation: n recursive calls due to insert_tree, n loops due to iteration in list, 2**n recursive calls due to flatten tree `
###########
# Task 3a #
###########
def sort_it(lst):
    tree = make_empty_tree()
    for i in lst:
        tree = insert_tree(i,tree)
    sort = flatten(tree)
    # Your code here
    return sort
###########
# Task 3b #
###########
# Time complexity of sort_it: O(n**2x2**n) where n is the max levels of the tree
# Explanation: n recursive calls due to insert_tree, n loops due to iteration in list, 2**n recursive calls due to flatten tree `




