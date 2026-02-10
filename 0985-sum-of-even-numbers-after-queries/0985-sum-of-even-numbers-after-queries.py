class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum(i for i in nums if i % 2 == 0)
        ans = []
        for val,index in queries:
            odd = True if nums[index] % 2 == 1 else False
            if odd:
                if (nums[index] + val) % 2 == 1:
                    nums[index] += val
                else:
                    nums[index] += val
                    summ += nums[index]
                ans.append(summ)
            else:
                if (nums[index] + val) % 2 == 1:
                    summ -= nums[index]
                    nums[index] += val
                else:
                    nums[index] += val
                    summ += val
                ans.append(summ)
        return ans