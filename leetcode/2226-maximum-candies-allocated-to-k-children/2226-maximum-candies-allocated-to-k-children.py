class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        

        def check(n):
            if n == 0:
                return True
            cur = 0

            for i in range(len(candies)):
                cur += candies[i]//n

            return cur >= k

        low = 0
        high = max(candies)

        #TTTTTTTTFFFFFFFFFFFFFFFFF

        ans = 0

        while low <= high:
            mid = (low+high)//2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans