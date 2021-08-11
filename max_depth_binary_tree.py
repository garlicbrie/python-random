class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

'''
       3
      / \
    9    20
         / \
        15  7

maxDepth(3):
  left_height = maxDepth(9) << 1
  right_height = maxDepth(20) << 2
  
  2+1

  --
maxDepth(20):
  left_height = 1
  right_height = 1
  max(1) + 2
--
maxDepth(15):
  left_height = 0
  right_height = 0

'''            