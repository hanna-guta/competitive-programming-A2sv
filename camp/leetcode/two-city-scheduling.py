class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        n = len(costs) // 2
        diff_costs = [(a - b, i) for i, (a, b) in enumerate(costs)]
        diff_costs.sort()

        for i in range(n):
            total_cost += costs[diff_costs[i][1]][0]

        for i in range(n, 2 * n):
            total_cost += costs[diff_costs[i][1]][1]

        return total_cost

        