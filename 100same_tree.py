from typing import Optional 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def PreOrderTraversal(self, root: Optional[TreeNode], result):
        if(root == None):
            result.append('null')
        elif(root != None):
            result.append(root.val)
            self.PreOrderTraversal(root.left, result)
            self.PreOrderTraversal(root.right, result)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_p = []
        visited_q = []

        self.PreOrderTraversal(p, visited_p)
        self.PreOrderTraversal(q, visited_q)

        if(visited_p == visited_q):
            result = True
        else: result = False
        return result


# Solution without DFS (dummy)
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if(p != None and q != None): print('current node {}, compared node {}'.format(p.val, q.val))
#         else: print('current node {}, compared node {}'.format(p, q))
#         if(p == None and q == None):
#             result = True
#         elif(p.val == q.val):
#             result = True
#             if(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):   
#                result = True
#         else:
#             result = False
#         print(result)
#         return result

sl = Solution()
p = TreeNode(1, left=TreeNode(1))
q = TreeNode(1, right=TreeNode(1))
print(sl.isSameTree(p, q))
            
        
        