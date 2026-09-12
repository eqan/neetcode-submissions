class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        sum = 0
        res = 0
        for R in range(len(arr)):
            if R - L >= k:
                sum -= arr[L]
                L+=1
            sum += arr[R]
            if (R - L + 1) == k and sum / k >= threshold:
                res += 1
        return res
