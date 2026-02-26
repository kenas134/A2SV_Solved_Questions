class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chk = {}
        for i in range(len(s)):
            if s[i] not in chk:
                chk[s[i]] = [i,i]
            else:
                chk[s[i]].pop()
                chk[s[i]].append(i)
        ans = list(chk.values())

        ans.sort()
        res = [ans[0]]
        end = ans[0][1]
        for i in range(1,len(ans)):
            left,right = ans[i]
            if end >= left:
                end = max(end,right)
                res[-1][1] = end
            else:
                res.append(ans[i])
                end = right
        s = []
        for i in range(len(res)):
            s.append(res[i][1]-res[i][0]+1)
        return s