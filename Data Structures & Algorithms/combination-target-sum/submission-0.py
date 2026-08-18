class Solution:
    def __init__(self):
        self.res = []
        self.subset = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr_total):
            if curr_total == target:
                self.res.append(self.subset.copy())
                return
            if i == len(nums) or curr_total > target:
                return
            self.subset.append(nums[i])
            dfs(i, curr_total+nums[i])
            self.subset.pop()
            dfs(i+1, curr_total)
        dfs(0, 0)
        return self.res