class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, nums[0]
        for n in nums:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum

        