class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx1 in range(len(nums)):
            for idx2 in range(len(nums)):
                if idx1 != idx2 and nums[idx1] == nums[idx2]:
                    return True
        return False