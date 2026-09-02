class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Heapify
        self.k = k
        heapq.heapify(nums)

        # Filter the excess elements early on
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums
    
    def add(self, val: int) -> int:
        # Add the element via the heap function
        heapq.heappush(self.nums, val)
        # Filter the excess elements
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # Return the first as its the largest
        return self.nums[0]