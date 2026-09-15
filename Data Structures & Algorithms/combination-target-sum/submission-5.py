class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr, total):
            if total == target:
                self.res.append(curr.copy())
                return
            if i>= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i+1, curr, total)

            return curr
        dfs(0, [], 0)
        return self.res


