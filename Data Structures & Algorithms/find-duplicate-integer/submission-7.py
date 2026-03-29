class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        time = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    time[i] += 1

        for i in range(1, len(nums)):
            for j in range(32):
                if i & (1 << j):
                    time[j] -= 1
        res = 0
        for i in range(32):
            if time[i] > 0:
                res |= (1 << i)
        return res
        
        