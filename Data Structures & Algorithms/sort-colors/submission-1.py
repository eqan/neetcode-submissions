class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        i = 0
        for color in range(3):
            for _ in range(counts.get(color, 0)):
                nums[i] = color
                i += 1