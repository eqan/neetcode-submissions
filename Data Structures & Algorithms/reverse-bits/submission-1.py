class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # Using the and operator to retain only the 1's discaeding the 0s, with the right shifting it helps us discard the elements on the right side
            res = res | (bit << (31 - i)) # Would be doing logic OR with the result and the computed result, the computed result we are doing a similar thing with the offset, now offset is and subtracting from 31(total number of bits) and then left shifting the bit
        return res
        