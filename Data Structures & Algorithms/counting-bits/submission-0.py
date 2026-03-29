class Solution:
    def countBits(self, n: int) -> List[int]:
        countArr = [0] * (n + 1)
        for i in range(n + 1):
            val = i
            while val:
                val &= val - 1
                countArr[i] += 1
        return countArr            