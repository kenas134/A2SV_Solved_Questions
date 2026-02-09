class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cN1 = None
        co1 = 0
        cN2 = None
        co2 = 0
        for i in nums:
            if i == cN1:
                co1 += 1
            elif i == cN2:
                co2 += 1
            elif co1 == 0:
                cN1 = i
                co1 = 1
            elif co2 == 0:
                cN2 = i
                co2 = 1
            else:
                co1 -= 1
                co2 -= 1
        ans = []
        if nums.count(cN1) > len(nums)/3:
            ans.append(cN1)
        if nums.count(cN2) > len(nums)/3:
            ans.append(cN2)
        return ans