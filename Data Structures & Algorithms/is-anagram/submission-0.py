class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r1 = {}
        r2 = {}
        if len(s) != len(t):
            return False
        else:
            for i,j in zip(s, t):
                if i not in r1:
                    r1[i] = 0
                else:
                    r1[i] += 1
                if j not in r2:
                    r2[j] = 0
                else:
                    r2[j] += 1
        for i in r1.keys():
            if i not in r2.keys() or r1[i] != r2[i]:
                return False
        return True
        