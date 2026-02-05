class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        chk = {}
        
        # store indices from list1
        for i in range(len(list1)):
            if list1[i] not in chk:
                chk[list1[i]] = i
        
        
        for i in range(len(list2)):
            if list2[i] in chk:
                chk[list2[i]] += i
        
        z = set(list2)
       
        chk = {k: v for k, v in chk.items() if k in z}
        
        
        ans = list(chk.items())
        ans.sort(key=lambda x: x[1])
        
        ans2 = set()
        val = ans[0][1]
        
        for i in ans:
            if i[1] == val:
                ans2.add(i[0])
            else:
                break
        
        return list(ans2)
