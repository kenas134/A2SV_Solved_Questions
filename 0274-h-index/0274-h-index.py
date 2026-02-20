class Solution:
    def hIndex(self, arr: List[int]) -> int:
        arr.sort()
        

        left = 0
        right = max(arr) + 1
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if len(arr)-bisect_left(arr,mid) >= mid:  
                ans = mid       
                left = mid + 1  
            else:  
                right = mid - 1 

        return ans