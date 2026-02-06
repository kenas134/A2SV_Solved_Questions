class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            s="".join(sorted(i))
            if s not in ans:
                ans[s]=[i]
            else:
                ans[s].append(i)
        return list(ans.values())
        