class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def bruteForce(nums):
            maxSum = nums[0]
            for i in range(len(nums)):
                currSum = 0
                for j in range(i, len(nums)):
                    currSum += nums[j]
                    maxSum = max(maxSum, currSum)
            return maxSum

        def kadanes(nums):
            currSum, maxSum = 0, nums[0]
            for n in nums:
                currSum = max(currSum, 0) # We filter the negative values
                currSum += n
                maxSum = max(currSum, maxSum)
            return maxSum
        return kadanes(nums)

        def slidingWindow(nums):
            maxSum, currSum, maxL, maxR, L = num[0], 0, 0, 0, 0
            for R in range(len(nums)):
                if currSum < 0:
                    currSum = 0
                    L = R
                currSum += nums[R]
                if currSum > maxSum:
                    maxSum = currSum
                    maxL,maxR = L, R
            return maxL, maxR
        
        return slidingWindows(nums)
