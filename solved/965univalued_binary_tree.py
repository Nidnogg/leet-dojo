# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    is_uni = True
    def preOrderTraversal(self, root, traversed):
        if(root != None):
            if(root.val not in traversed and len(traversed) > 0):
                print(root.val)
                self.is_uni = False
            else:
                traversed.append(root.val)
                self.preOrderTraversal(root.left, traversed)
                self.preOrderTraversal(root.right, traversed)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        traversed = []
        self.is_uni = True
        self.preOrderTraversal(root, traversed)
        if(self.is_uni == False): 
            return False
        else: return True
