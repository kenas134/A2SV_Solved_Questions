class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        arr = list(dic.items())
        sorted_dict = sorted(arr,key=lambda x:x[1],reverse=True)
        list1 = [i for i,j in sorted_dict]
        return list1[:k]
        