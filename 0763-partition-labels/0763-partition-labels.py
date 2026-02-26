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
        res = [ans[0][1] - ans[0][0] + 1]
        start = ans[0][0]
        end = ans[0][1]
        for i in range(1,len(ans)):
            left,right = ans[i]
            if end >= left:
                end = max(end,right)
                res.pop()
                res.append(end-start+1)
            else:
                res.append(right-left+1)
                start = ans[i][0]
                end = ans[i][1]

        return res