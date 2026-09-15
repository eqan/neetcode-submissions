class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        for c in range(3):
            while count[c] > 0:
                nums[i] = c
                count[c]-=1
                i+=1



