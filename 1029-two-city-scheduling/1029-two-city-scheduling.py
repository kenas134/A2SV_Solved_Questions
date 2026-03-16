class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

        ans = 0
        costs.sort(key=lambda x:x[0]-x[1])

        i = 0
        j = len(costs)-1

        while i < j:
            ans += costs[i][0]
            ans += costs[j][1]
            i += 1
            j -= 1
        return ans