from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        return self.traverse(root, result)
           
    def traverse(self, root: Optional[TreeNode], result):
        if(root != None):
            result.append(root.val)
            self.traverse(root.left, result)
            self.traverse(root.right, result)
        return result
  
sl = Solution()
p = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))       
print(sl.preorderTraversal(p))



        
            
        
        
        