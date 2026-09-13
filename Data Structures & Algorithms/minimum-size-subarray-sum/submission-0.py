class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        k = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                k = min(k, R - L + 1)
                total -= nums[L]
                L += 1 
        return 0 if k == float('inf') else k
