from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Reverse Iterative preorder, slightly better performance
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack =[]
        cur = root
        
        while cur or stack:
            if cur :
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res[::-1]
# Incredibly bad performance/memory for some reason.
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
#         result = []
#         return self.traverse(root, result)
           
#     def traverse(self, root: Optional[TreeNode], result):
#         if(root != None):
#             self.traverse(root.left, result)
#             self.traverse(root.right, result)
#             result.append(root.val)
#         return result
  
sl = Solution()
p = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))       
print(sl.preorderTraversal(p))



        
            
        
        
        