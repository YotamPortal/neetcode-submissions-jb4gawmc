class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(k):
            totalTime = 0
            for n in piles:
                totalTime += math.ceil(n / k)
            return totalTime

        lowK, maxK = 1, max(piles)
        minK = maxK
        while lowK <= maxK:
            mid = lowK + (maxK - lowK) // 2
            K = totalTime(mid)
            if K > h:
                lowK = mid + 1
            else: # K <= h:
                maxK = mid - 1
                minK = mid
        
        return minK
