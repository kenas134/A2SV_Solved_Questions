class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def check(n):
            last = position[0]
            left = m-1

            for i in range(1,len(position)):
                if position[i] - last >= n:
                    last = position[i]
                    left -= 1
                if left == 0:
                    return True
            return left <= 0


        position.sort()

        high = position[-1]-position[0]
        low = 1

        ans = 0

        while low <= high:
            mid = (low+high)//2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
