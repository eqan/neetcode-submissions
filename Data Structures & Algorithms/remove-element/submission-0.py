class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_idx = 0
        for read_idx in range(len(nums)):
            if nums[read_idx] != val:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
        return write_idx
