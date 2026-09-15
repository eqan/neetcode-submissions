class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n+1, ....]
        # Rob2 is the last house we rob
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

