class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()

        def can(n):
            j = 0
            i = 0
            while i < len(houses) and j < len(heaters):
                rang = [heaters[j]-n,heaters[j]+n]
                if rang[0] <= houses[i] <= rang[1]:
                    i += 1
                else:
                    j += 1
                    
            if i == len(houses):
                return True
            return False

            

                
        low = 0
        high = max(houses[-1]-heaters[0] , heaters[-1]-houses[0])
        ans = -1

        while low <= high:

            mid = (low+high)//2
            if can(mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1
        return ans