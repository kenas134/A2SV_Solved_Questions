class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = deque()
        res = []
        for i in range(k):
            while ans and ans[-1] < nums[i]:
                ans.pop()
            ans.append(nums[i])
        res.append(ans[0])
        left = 0
        for i in range(k,len(nums)):
            while ans and ans[-1] < nums[i]:
                ans.pop()
            ans.append(nums[i])
            if ans[0] == nums[left]:
                ans.popleft()
            res.append(ans[0])
            left += 1
        return res

        