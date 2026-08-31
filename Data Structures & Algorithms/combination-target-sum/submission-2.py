class Solution:
    def __init__(self):
        self.res = []
        self.subset = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Very similar to the prior solution but this time we cut off the dfs when total compares to target. Furthermore we are trying to find only the unique combinations
        def dfs(i, cur, total):
            # Recursive base cases
            # 1 if total is equal to target
            if total == target:
                self.res.append(cur.copy())
                return
            # 2 if total is bigger or equal than target and current ith level is bigger or equal to 
            if total > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return self.res


