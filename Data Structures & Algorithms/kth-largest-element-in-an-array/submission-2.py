import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums] # max heap
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)

        