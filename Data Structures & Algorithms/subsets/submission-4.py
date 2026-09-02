from typing import List
class Solution:
    def __init__(self):
        self.res = []
        self.subset = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            # Base case when the current ith iteration exceeds the length of nums
            if i >= len(nums):
                self.res.append(self.subset.copy())
                return

            # First adding a new element for DFS(variation with)
            self.subset.append(nums[i])
            dfs(i+1)

            # Now removing the element for DFS(variation without)
            self.subset.pop()
            dfs(i+1)

        
        # When the question asks for all possible solutions there is a high possibility of using DFS and recursive solutions
        dfs(0)
        return self.res
