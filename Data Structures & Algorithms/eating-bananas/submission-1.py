class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatForK(k):
            eatSum = 0
            for n in piles:
                eatSum += math.ceil(n / k)
            return eatSum

        piles.sort()
        lowK, maxK = 1, max(piles)
        minK = maxK
        while lowK <= maxK:
            mid = lowK + (maxK - lowK) // 2
            K = eatForK(mid)
            if K > h:
                lowK = mid + 1
            elif K <= h:
                maxK = mid - 1
                minK = min(minK, mid)
        
        return minK
