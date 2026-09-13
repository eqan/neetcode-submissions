class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L, maxLen, maxF = 0, 0, 0
        for R in range(len(s)):
            if s[R] not in count:
                count[s[R]] = 1
            else:
                count[s[R]] += 1
            currWinSize = R - L + 1
            maxF = max(maxF, count[s[R]])
            res = currWinSize - maxF
            if res <= k:
                maxLen = max(maxLen, currWinSize)
            else:
                count[s[L]] -= 1
                L+=1
        return maxLen
            

        