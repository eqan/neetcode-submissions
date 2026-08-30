class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1,max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            _h = self.calculateFeasible(piles, k)
            if _h <= h:
                res = k
                r = k - 1 # Trye to find a smaller range
            else:
                l = k + 1 # Need a faster rate
        return res 

    
    def calculateFeasible(self, piles, h):
        res = 0
        for x in piles:
            res += math.ceil(x/h)
        return res
