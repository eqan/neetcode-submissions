import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Simulating max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x- y)
        stones.append(0) # avoid 0 error
        return abs(stones[0])


        