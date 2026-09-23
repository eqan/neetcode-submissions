class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, cur_max = 0, 0
        for n in nums:
            if n == 0:
                cur_max = max(cur_max, curr)
                curr = 0
            else:
                curr += 1
        cur_max = max(cur_max, curr)
        return cur_max

