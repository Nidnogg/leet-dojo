# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    maxDepthCounter = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return self.maxDepthCounter
        self.maxDepthCounter
        self.traverse(root, self.maxDepthCounter)
        return self.maxDepthCounter

    def traverse(self, root: Optional[TreeNode], depth):
        if root != None:
            curDepth = depth + 1
            if curDepth > self.maxDepthCounter:
                self.maxDepthCounter = curDepth
            self.traverse(root.left, curDepth)
            self.traverse(root.right, curDepth)


