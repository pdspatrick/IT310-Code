class Node:
    """Simple node class for singly-linked list"""
    def __init__(self, value, next=None):
        """Create a new node, with optional next node pointer"""
        self.value = value
        self.next = next
    def __repr__(self):
        if self.next is not None:
            return str(str(self.value) + "," + str(repr(self.next)))
        else:
            return str(self.value)
    def toList(self):
        return [int(x) for x in str(self.__repr__()).split(',') if x]

def stalin_sort(node):
    """Implement StalinSort"""
    if node is not None:
        # This is the stupid way, but it works.
        if node.next is not None:
            if node.value > node.next.value:
                node.next = node.next.next
                stalin_sort(node.next)
                if node.next is not None:
                    if node.value > node.next.value:
                        node.next = node.next.next
                        stalin_sort(node.next)
                        if node.next is not None:
                            if node.value > node.next.value:
                                node.next = node.next.next
                                stalin_sort(node.next)
            else:
                stalin_sort(node.next)
    print(node)
    return node

n4 = Node(20)
n3 = Node(10,n4)
n2 = Node(30,n3)

print(n2.toList())
stalin_sort(n2)
print(n2.toList())