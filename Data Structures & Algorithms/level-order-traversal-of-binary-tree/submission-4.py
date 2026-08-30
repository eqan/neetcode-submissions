# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            # This array will help us to store only values(which is required not nodes) level by level
            surface_level = []
            for _ in range(len(queue)):
                # Pop first from the queue, we will add nodes 1 by 1 to surface level, as the original length would change so surface_level would only contain elements that were inbound
                node = queue.popleft()
                surface_level.append(node.val)

                # If there's left node add it to the queue
                if node.left:
                    queue.append(node.left)

                # If there's right node add it to the queue
                if node.right:
                    queue.append(node.right)

            # After the surface level array has the elements then append it into the result
            res.append(surface_level)
        return res
                    
