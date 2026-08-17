from typing import List
class Solution:
    def __init__(self):
        self.res = []
        self.subset = []
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Exclude nums[i] (backtrack)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res