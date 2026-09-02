# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the root node is None that means we reached end and no targetSum was found then return false
        if root is None:
            return False
        # Append the current root value into the path
        self.path.append(root.val)
        # If we reach absolute leaf node and the sum of the path is equal to target return True
        if root.left is None and root.right is None and sum(self.path) == targetSum:
            return True
        '''
            Recursive call on the children
        '''
        # If the call stack return true then return true
        if self.hasPathSum(root.left, targetSum):
            return True
        # If the call stack return true then return true
        if self.hasPathSum(root.right, targetSum):
            return True
        # BackTrack: remove current node before returning
        self.path.pop()
        return False