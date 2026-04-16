class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_max, absolute_max = 0, 0
        for n in nums:
            if n == 0:
                if current_max > absolute_max:
                    absolute_max = current_max
                current_max = 0
            else:
                current_max += 1
        if current_max > absolute_max:
            return current_max
        return absolute_max        