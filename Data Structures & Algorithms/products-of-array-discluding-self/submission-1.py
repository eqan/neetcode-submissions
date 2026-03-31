class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        value = 1
        for i in range(len(nums)):
            result[i] = value
            value *= nums[i]
        value = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= value
            value *= nums[i]
        return result

        