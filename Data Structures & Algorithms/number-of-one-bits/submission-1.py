class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1: # check if the LSB of n is 1
                count += 1
            n = n >> 1 # right shift every bit one position to the right

        return count
