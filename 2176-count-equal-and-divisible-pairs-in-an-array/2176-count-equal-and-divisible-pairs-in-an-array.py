class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        chk = defaultdict(list)
        for index,value in enumerate(nums):
            chk[value].append(index)
        
        count = 0
        for indexs in chk.values():
            m = len(indexs)
            for i in range(m):
                for j in range(i+1,m):
                    if indexs[i]*indexs[j] % k == 0:
                        count += 1
        return count 

