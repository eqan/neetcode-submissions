class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            # The right sum would be when you subtract the total with the left sum and the current number
            rightSum = total - leftSum - nums[i]
            # You know that lol
            if leftSum == rightSum:
                return i
            # Left sum incrementally made up as we move along
            leftSum += nums[i]
        return -1
