class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brute Force Technique
        # def dfs(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i+1, j+1)
        #     else:
        #         return max(dfs(i+1, j), dfs(i, j+1))
        # return dfs(0, 0)

        # Top-Bottom - Memoization
        memo = {}    
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i+1, j+1) 
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return memo[(i, j)]

        # Bottom Up - True DP
        def bottomUp(m, n):
            matrix = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if text1[i] == text2[j]:
                        matrix[i][j] = 1 + matrix[i+1][j+1]
                    else:
                        matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
            return matrix[0][0]
        m, n = len(text1), len(text2)
        # return bottomUp(m, n)
        return dfs(0, 0)