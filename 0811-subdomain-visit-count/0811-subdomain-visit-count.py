class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dicts = {}
        for urls in cpdomains:
            num,url1 = urls.split()
            url = url1.split(".")
            for i in range(len(url)):
                s = ".".join(url[i:])
                if s in dicts:
                    dicts[s] += int(num)
                else:
                    dicts[s] = int(num)
        ans = [f"{v} {k}" for k , v in dicts.items()]
        return ans
