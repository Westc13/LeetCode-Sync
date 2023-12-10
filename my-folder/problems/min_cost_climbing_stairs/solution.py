class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [0] * len(cost)
        result[0] = cost[0]
        result[1] = cost[1]

        for i in range(2, len(cost)):
            result[i] = cost[i] + min(result[i-1], result[i-2])
        return min(result[-1], result[-2])