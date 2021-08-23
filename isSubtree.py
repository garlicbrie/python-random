# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        isSame(p, q):
        
        '''
        def isSame(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            if p.val == q.val:
                left= isSame(p.left, q.left)
                right= isSame(p.right, q.right)
                return left and right
        
        return isSame(root, subRoot)
            
        