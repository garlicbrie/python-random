class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def visit(node):
    if not node:
        return

    visit(node.left)
    print(node.val)
    visit(node.right)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

two.left = one
two.right = three

six.left = five
six.right = seven

four.left = two
four.right = six

visit(four)


