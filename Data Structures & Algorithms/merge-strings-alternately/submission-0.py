class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       longest = ""
       shortest_length = 0
       res = ""
       if len(word2) > len(word1):
            longest = "w2"
            shortest_length = len(word1)
       else:
            longest = "w1"
            shortest_length = len(word2)
       l = 0
       while l < shortest_length:
            res += word1[l]
            res += word2[l]
            l+=1
       if longest == "w2":
            res += word2[l:]
       else:
            res += word1[l:]
       return res

            
