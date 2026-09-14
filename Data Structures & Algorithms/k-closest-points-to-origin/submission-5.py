import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, minHeap = [], []
        for x, y in points:
            dis = (x**2) + (y**2)
            res.append([dis, x, y])
        heapq.heapify(res)
        while k > 0:
            dis, x, y = heapq.heappop(res)
            minHeap.append([x, y])
            k-=1
        return minHeap