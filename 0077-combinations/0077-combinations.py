class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def back_track(i,arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            if i > n:
                return
            arr.append(i)
            back_track(i+1,arr)
            arr.pop()
            back_track(i+1, arr)
        back_track(1,[])
        return ans

            
            