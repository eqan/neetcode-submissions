class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Brute Force Method
        def bruteForce():
            for L in range(len(nums)): # Starting left pointer
                for R in range(L+1, min(len(nums), L+k+1)): # Right pointer starting after L and remains inbound the sliding window range or total length of nums
                    if nums[L] == nums[R]: # If value compares return True
                        return True
            return False

        #return bruteForce()

        # Memoize method to cache results we already crossed
        def memoize():
            window = set()
            L = 0
            for R in range(len(nums)):
                if R - L > k:
                    window.remove(nums[L])
                    L+=1
                if nums[R] in window:
                    return True
                window.add(nums[R])
            return False
        return memoize()


        