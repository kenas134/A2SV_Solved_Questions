class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum(i for i in nums if i % 2 == 0)
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                summ -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                summ += nums[idx]

            ans.append(summ)
        return ans