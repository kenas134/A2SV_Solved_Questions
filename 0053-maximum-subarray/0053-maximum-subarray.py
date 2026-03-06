class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        pref = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            pref.append(summ)


        minn = 0

        ans = float("-inf")

        for i in range(len(nums)):
            cur = pref[i]
            

            if cur < minn:
                ans = max(ans,cur-minn)
                minn = cur

            else:
                ans = max(cur-minn,ans)

        return ans




        