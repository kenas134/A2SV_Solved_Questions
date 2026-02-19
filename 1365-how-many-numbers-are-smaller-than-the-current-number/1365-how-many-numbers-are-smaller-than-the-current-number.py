class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        j = 1
        ans = [0]
        for i in range(1,len(nums)):
            if arr[i-1] < arr[i]:
                ans.append(j)
                j += 1
            else:
                j += 1
                ans.append(ans[-1])

        chk = {}
        for i in range(len(nums)):
            chk[arr[i]] = ans[i]
        l = []
        for i in range(len(nums)):
            l.append(chk[nums[i]])
        return l

