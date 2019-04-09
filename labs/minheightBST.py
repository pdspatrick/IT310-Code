class TreeNode:
    '''Node for a simple binary tree structure'''
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def min_height_BST(alist):
    '''Returns a minimum-height BST built from the elements in alist (which are in sorted order)'''
    # I think we can just keep finding the middle....right?
    # and contiunually pass smaller lists recursively.
    # Trying to do this without try/except ended up with
    # Zybooks giving me a funny looking stack overflow error.
    middle = (len(alist) // 2)
    try:
        boop = TreeNode(alist[middle], None, None)
        boop.left = min_height_BST(alist[:middle])
        boop.right = min_height_BST(alist[middle+1:])
    except:
        pass
    return boop
        
        