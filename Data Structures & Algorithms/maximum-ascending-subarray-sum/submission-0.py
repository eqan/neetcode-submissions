class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_res = 0
        local_res = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                local_res += nums[i+1]
            else:
                max_res = max(local_res, max_res)
                local_res = nums[i+1]
        return max(max_res, local_res)
