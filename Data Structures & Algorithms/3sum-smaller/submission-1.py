class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
       nums.sort()
       res = 0
       for i in range(len(nums)-2):
           res += self.twoSumSmaller(nums, i+1, target - nums[i])
       return res
    
    def twoSumSmaller(self, nums, start, target):
        left = start
        right = len(nums) - 1
        count = 0
        while left < right:
            if (nums[left] + nums[right]) < target:
                count += right - left
                left+=1
            else:
                right-=1
        return count
