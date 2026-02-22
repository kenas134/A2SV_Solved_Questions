class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def back_track(i,arr):

            if i == len(nums):
                ans.append(arr[:])
                return

            arr.append(nums[i])
            back_track(i+1,arr)
            arr.pop()
            back_track(i+1,arr)
        back_track(0,[])
        return ans
