import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negative numbers to simulate max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Get the two heaviest stones (most negative values)
            x = heapq.heappop(stones)  # -y (heaviest)
            y = heapq.heappop(stones)  # -x (second heaviest)
            
            if x != y:  # If x == y, both are destroyed
                # Push back the remaining stone (remember values are negated)
                heapq.heappush(stones, x - y)  # -(y-x)
        
        # Return 0 if no stones left, otherwise return the last stone's weight
        return abs(stones[0]) if stones else 0
            