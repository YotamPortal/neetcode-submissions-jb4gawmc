class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCostArr = [0] * (n)
        minCostArr[0], minCostArr[1] = cost[0], cost[1]
        for i in range(2, n):
            minCostArr[i] = min(minCostArr[i-1], minCostArr[i-2]) + cost[i]

        return min(minCostArr[n-1], minCostArr[n-2])