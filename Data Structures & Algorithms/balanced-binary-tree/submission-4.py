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
            isBL, hL = dfs(root.left)
            isBR, hR = dfs(root.right)
            computedHeight = abs(hL - hR)
            if isBL and isBR and computedHeight <= 1:
                return [True, 1+ max(hL, hR)]
            return [False, 1 + max(hL, hR)]
        return dfs(root)[0]