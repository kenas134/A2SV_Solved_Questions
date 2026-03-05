class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        

        chk = {0:-1}
        summ = 0
        for i in range(len(nums)):

            summ += nums[i]
            left = summ %  k
            if left in chk:
                if i - chk[left] >= 2:
                    return True
            else:
                chk[left] = i
        return False