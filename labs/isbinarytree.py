from collections import deque
class TreeNode:
    '''Node for a simple binary tree structure'''
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
def isBinarySearchTree(tree):
    if tree is not None:
        if tree.left and tree.right is None:
            return True
        if tree.left and tree.right is not None:
            if tree.left.value >= tree.right.value:
                return False
            else:
                if isBinarySearchTree(tree.left) is False:
                    return False
                if isBinarySearchTree(tree.right) is False:
                    return False
            if tree.left.value >= tree.value or tree.right.value <= tree.value:
                return False
        if tree.left is not None:
            if tree.right is None:
                if tree.left.value < tree.value:
                    return True
                else:
                    return False
            if tree.left.right is not None:
                if tree.left.right.value >= tree.value:
                    return False
        if tree.right is not None:
            if tree.left is None:
                if tree.right.value > tree.value:
                    return True
                else:
                    return False
            if tree.right.left is not None:
                if tree.right.left.value >= tree.value:
                    return False

    return True