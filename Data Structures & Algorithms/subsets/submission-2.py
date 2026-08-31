from typing import List
class Solution:
    def __init__(self):
        self.res = []
        self.subset = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i >= len(nums):
                self.res.append(self.subset.copy())
                return

            # First adding a new element for DFS(variation with)
            self.subset.append(nums[i]) 
            dfs(i+1) 

            # Now removing the element for DFS(variation without)
            self.subset.pop()
            dfs(i+1)
        dfs(0)
        return self.res
