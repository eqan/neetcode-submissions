class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # We move the good values to the start so basically, k the slow pointer is on the position where potential bad values can be and furthermore, the good values need to be swapped on the start of the arra
                k += 1
        return k
