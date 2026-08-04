class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        w_c = 0
        op = float('inf')

        for r in range(len(blocks)):
            if blocks[r] == "W":
                w_c += 1
            if r -  l + 1 > k:
                if blocks[l] == "W":
                    w_c -= 1
                l+=1
            if r - l + 1 >= k:
                op = min(op, w_c)
        return op