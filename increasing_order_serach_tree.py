'''
      5
    /   \
   4     3
  / \     \
 1   2     6

 inorder = 1, 4, 2, 5, 3, 6


call stack: 

helper(5):
  res = helper(4, 5)  = [1, 4, 2, 5]

--
helper(4, 5):
  res = helper(1, 4) = [1, 4]
  4.left = None
  4.right = helper(2, 5) = [2, 5]
  return [1, 4, 2, 5]

--
helper(2, 5):
  res = helper(None, 2) = 2
  2.left = None
  2.right = helper(None, 5) = 5
  return [2, 5]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(root, tail = None):
            # at leaf node, alway return itself
            if not root: return tail
            # recursive call with left value as root and current value as tail (next value)
            res = helper(root.left, root)
            # we are only chaining it to the right, nothing on the left
            root.left = None
            # recursive call with right value as root and tail as tail. 
            # if the current node is a left child, the tail is parents from helper(root.left, root) this line
            # if the current node is a right child, the tail is parents' parents (?)
            root.right = helper(root.right, tail)
            return res
        
        return helper(root)