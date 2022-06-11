# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderTraversal(self, root, traversed):
        if(root != None):
            if(root.val not in traversed and len(traversed) > 0):
                print(root.val)
                return False
            else:
                traversed.append(root.val)
                self.preOrderTraversal(root.left, traversed)
                self.preOrderTraversal(root.right, traversed)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        traversed = []
        is_uni = self.preOrderTraversal(root, traversed)
        
        if(is_uni == None): 
            return False
        else: return True
