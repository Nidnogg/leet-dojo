# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.traverse(root, result)

    def traverse(self, root: Optional[TreeNode], result, maxDepth):
        if(root != None):
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)
        return result
