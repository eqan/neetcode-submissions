class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):# 1 is the starting poing and we used n+1 because i will go upto n not n+1
            if offset * 2 == i: # We check if doubling the offset reaches the value to the current number that means we reached a more significant bit value i.e from [1,2,4,8,16....]
                offset = i
            # Formulat dp[n] = 1 + dp[n - offset]
            dp[i] = 1 + dp[i - offset]
        return dp