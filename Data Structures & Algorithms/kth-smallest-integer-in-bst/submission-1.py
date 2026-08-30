# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:

            # As smallest k's are on the left side add them up
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the node to the top of stack
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right