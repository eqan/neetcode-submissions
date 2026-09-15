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
        '''
            In backtracking there's a concept that if there's a mutable shared list in recursive function we have to undo the changes before returning to the parent call
            1.  Choose: Add the current node (path.append(node.val))
            2. Explore: Recurse on the left and right children
            3. Un-choose: Remove the node (path.pop()) so other branches don't see it
        '''
        # BackTrack: remove current node before returning
        self.path.pop()
        return False