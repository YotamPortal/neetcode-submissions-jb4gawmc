class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            temp = second
            second = min(first, temp) + cost[i]
            first = temp
        return min(first, second)
