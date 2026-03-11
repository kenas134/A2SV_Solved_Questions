class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        Dec = deque()
        Inc = deque()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while Dec and Dec[-1] < nums[r]:
                Dec.pop()
            Dec.append(nums[r])
            while Inc and Inc[-1] > nums[r]:
                Inc.pop()
            Inc.append(nums[r])

            while Dec[0] - Inc[0] > limit:
                if nums[l] == Dec[0]:
                    Dec.popleft()
                if nums[l] == Inc[0]:
                    Inc.popleft()
                l += 1
            ans = max(ans,r-l+1)
        return ans
            

            