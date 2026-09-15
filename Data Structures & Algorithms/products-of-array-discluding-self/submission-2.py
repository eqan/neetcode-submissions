class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        val = 1
        for i,n in enumerate(nums):
            res[i] = val
            val *= n
        val = 1
        # This has to be done in reverse
        for i in range(len(nums)-1, -1, -1):
            res[i] *= val
            val *= nums[i]
        return res

