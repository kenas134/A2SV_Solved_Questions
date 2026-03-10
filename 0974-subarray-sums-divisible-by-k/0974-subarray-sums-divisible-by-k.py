class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            pref.append(summ)
        chk  = {0:1}
        ans = 0
        for i in range(len(nums)):
            remainder = pref[i] % k
            ans += chk.get(remainder,0)
            chk[remainder] = chk.get(remainder,0) + 1
        return ans



