class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        z_c = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z_c +=1

            while z_c > k:
                if nums[l] == 0:
                    z_c -= 1
                l+=1
            max_len = max(max_len, r-l+1)
        return max_len