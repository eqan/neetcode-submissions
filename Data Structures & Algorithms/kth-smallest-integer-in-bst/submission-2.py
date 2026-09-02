# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            # Getting all the smallest from this tree
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process one node(the current smallest) 
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            
            # Else if we dont find anything we turn to the right
            curr = curr.right
            
        return res
