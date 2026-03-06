class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        chk = {0:1}
        ans = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            need = summ - goal
            if  need in chk:
                ans += chk[need]
            chk[summ] = chk.get(summ,0) + 1

        return ans


        