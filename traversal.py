'''
      5
    /   \
   4     3
  / \     \
 1   2     6

preorder = visit, left, right -> 5, 4, 1, 2, 3, 6 [starts at root, ends at rightmost node]
* when you need to visit root before its children

inorder = left, visit, right -> 1, 4, 2, 5, 3, 6 [starts at leftmost node, ends at rightmost node]
* sequencing

postorder = left, right, visit -> 1, 2, 4, 6, 3, 5 [starts at leftmost node, ends at root]
* when you need to visit all the children before the root
'''

# inorder
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


