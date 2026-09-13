class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L, maxLen, maxF = 0, 0, 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxF = max(maxF, count[s[R]])
            windowLen = R - L + 1
            if windowLen - maxF > k:
                count[s[L]] -= 1
                L += 1
            else:
                maxLen = max(maxLen, windowLen)
        return maxLen
