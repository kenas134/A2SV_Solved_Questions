class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        arr = [0]*(len(nums)+1)

        for i in range(len(nums)):
            arr[nums[i]] += 1
        missing = 0
        double = 0

        for i in range(1,len(nums)+1):
            if arr[i] == 0:
                missing = i
            if arr[i] == 2:
                double = i

        return [double,missing]

