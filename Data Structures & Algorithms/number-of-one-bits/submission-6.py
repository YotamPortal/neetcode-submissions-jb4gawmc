class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1) # Brian Kernighan’s Algorithm - 
            count = count + 1
        return count