class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Very similar to the prior solution but this time we cut off the dfs when total compares to target. Furthermore we are trying to find only the unique combinations
        def dfs(i, cur, total):
            # Recursive base cases
            # 1 if total is equal to target
            if target == total:
                self.res.append(cur.copy())
                return
            # 2 if total is bigger than target or current ith level is bigger or equal to the total size of nums 
            if total > target or i >= len(nums):
                return
            # Adding the same element(left branch) 
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # Moving forward without the same element added(right branch) 
            cur.pop()
            # But here you can see we move forward using the next element(i+1)
            dfs(i+1, cur, total)
        # Starting with 0
        dfs(0, [], 0)
        return self.res


