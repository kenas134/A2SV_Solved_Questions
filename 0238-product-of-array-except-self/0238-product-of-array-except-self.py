class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        forward = []
        back = []
        pr = 1
        for i in range(len(nums)):
            pr *= nums[i]
            forward.append(pr)

        pr = 1

        for i in range(len(nums)-1,-1,-1):
            pr *= nums[i]
            back.append(pr)
        back.reverse()
        ans = []

        for i in range(len(nums)):
            if i == len(nums)-1:
                ans.append(forward[i-1])
            elif i == 0:
                ans.append(back[i+1])
            else:
                ans.append(forward[i-1]*back[i+1])

        return ans

