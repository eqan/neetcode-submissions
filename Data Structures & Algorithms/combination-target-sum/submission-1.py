class Solution:
    def __init__(self):
        self.res = []
        self.subset = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, cur, total):
            if total == target:
                self.res.append(cur.copy())
                return
            if total >= target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return self.res


