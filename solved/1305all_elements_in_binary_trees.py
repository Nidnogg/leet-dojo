# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderTraversal(self, root: TreeNode, result):
        if(root != None):
            result.append(root.val)
            self.preOrderTraversal(root.left, result)
            self.preOrderTraversal(root.right, result)
            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        fake_root = TreeNode(0, left=root1, right=root2)
        self.preOrderTraversal(fake_root, result)
        result.pop(0)
        result.sort()
        return result        