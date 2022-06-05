from __future__ import annotations
from typing import Optional

from matplotlib.cbook import ls_mapper

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        local_result = []
        self.traverse(root, local_result)
        return local_result
        
    def traverse(self, root: Optional[TreeNode], local_result):
        if(root != None):
            local_result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
  
sl = Solution()
p = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))       

print(sl.preorderTraversal(p))

        
            
        
        
        