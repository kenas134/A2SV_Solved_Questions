class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = Counter()
        count[0] = 1
        summ = 0
        ans = 0
        for i in range(len(nums)):
            summ += nums[i]
            need = summ - k

            if need in count:
                ans += count[need]
                count[summ] += 1
            else:
                count[summ] += 1

        return ans