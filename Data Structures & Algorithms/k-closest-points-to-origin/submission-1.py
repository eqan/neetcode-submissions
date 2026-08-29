class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x, y in points:
            dis = (x ** 2) + (y ** 2)
            minheap.append([dis, x, y])
        heapq.heapify(minheap)
        while k > 0:
            dis, x, y = heapq.heappop(minheap) # Remove smallest element using this, with .pop you would pop the largest element.
            res.append([x,y])
            k-=1
        return res