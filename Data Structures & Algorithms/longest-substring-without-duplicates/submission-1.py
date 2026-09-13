class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        L, maxSum = 0, 0
        for R in range(len(s)):
            while s[R] in check:
                check.remove(s[L])
                L+=1
            check.add(s[R])
            maxSum = max(maxSum, R - L + 1)
        return maxSum
