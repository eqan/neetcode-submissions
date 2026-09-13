class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1 # We started from 1 because we are standing at the first occurence
            while r+1 < len(nums) and nums[r] == nums[r+1]: # With this loop we count the total consecutive numbers and have r reach the last of the consecutive values
                r+=1
                count+=1
            for i in range(min(2, count)): # Using minumum we leave the left pointer to an index which exceeds the minimum 2
                nums[l] = nums[r] # Place the current R(that is at the end of the consecutive sequence) at the L index(that would be the at the index where it stopped last time)
                l+=1
            r += 1 # R pointer traverses to the next new number in the array
        return l
