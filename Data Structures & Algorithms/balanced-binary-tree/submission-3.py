# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> [bool, int]: # Return type is balanced|!balanced, height
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            # Checking if balanced, as we already have data from left[0] and right[0] whether the above tree branches were balanced and then using values of left and right we check post substraction their result is equal to or smaller than 1 which means its balanced to this point
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # From the above we now know we are balanced or not at this stage and for the tree height just pick the max from left or right and add 1 to it for the current height
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]



        