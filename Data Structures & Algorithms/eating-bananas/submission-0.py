class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(1, max(piles))
        res = r
        while l <= r:
            mid = (l+r)//2
            _h = self.calculateFeasible(piles, mid)
            if _h <= h:
                res= mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def calculateFeasible(self, piles, k):
        total = 0
        for p in piles:
            total += (p + k - 1) // k
        return total