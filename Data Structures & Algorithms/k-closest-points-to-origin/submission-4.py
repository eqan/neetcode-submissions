import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = [] 
        # Calculate
        for p in points:
            x, y = p[0], p[1]
            dis = (x**2) + (y**2) # Squaring them would eliminate the negative edge cases
            res.append([dis, x, y])
        heapq.heapify(res)
        while k > 0:
            dis, x, y = heapq.heappop(res)
            minHeap.append([x, y])
            k-=1
        return minHeap

