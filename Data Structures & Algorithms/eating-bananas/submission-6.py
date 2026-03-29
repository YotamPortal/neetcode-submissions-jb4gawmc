class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(k):
            totalTime = 0
            for n in piles:
                totalTime += math.ceil(n / k)
            return totalTime

        l, r = 1, max(piles)
        minK = r
        while l <= r:
            k = l + (r - l) // 2
            tTime = totalTime(k)
            if tTime > h:
                l = k + 1
            else: # tTime <= h:
                r = k - 1
                minK = k
        
        return minK
