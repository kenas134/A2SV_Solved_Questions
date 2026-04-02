class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(minweight):
            taken = 0
            dayy = 0
            for i in range(len(weights)):
                taken += weights[i]
                if taken > minweight:
                    dayy += 1
                    taken = weights[i]
            if taken > 0:
                dayy += 1
            return dayy <=days
        low , high = max(weights),sum(weights)
        ans = high
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        