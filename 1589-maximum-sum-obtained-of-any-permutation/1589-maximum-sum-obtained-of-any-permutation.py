class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref = [0] * (n+1)

        for i in range(len(requests)):
            l,r = requests[i]

            pref[l] += 1
            pref[r+1] -= 1

        for i in range(1,n):
            pref[i] = pref[i-1] + pref[i]
        pref = pref[:-1]
        pref.sort()
        nums.sort()
        ans = 0

        for i in range(n):
            ans += (pref[i]*nums[i])

        return ans % (10**9 + 7)




