class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        chk = {}

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                cur = stack.pop()
                chk[cur] = nums2[i]
            stack.append(nums2[i])
        
        for cur in stack:
                chk[cur] = -1
        ans = []
        for i in range(len(nums1)):
            ans.append(chk[nums1[i]])
        return ans
