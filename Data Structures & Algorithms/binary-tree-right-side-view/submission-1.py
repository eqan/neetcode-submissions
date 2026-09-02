# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        result = []
        '''
            Same solution as the level order but only thing is we add the right most element into the final result array from the surface level array(level_array)
        '''
        while len(queue) > 0:
            level_array = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_array.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level_array[-1])
        return result
        