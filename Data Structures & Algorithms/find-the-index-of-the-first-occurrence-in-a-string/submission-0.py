class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for start in range(len(haystack)):
            c = 0
            i = start
            j = 0
            while j < n and i < len(haystack) and  needle[j] == haystack[i]:
                    i+=1
                    j+=1
                    c +=1
            if c == n:
                return start
        return -1

        