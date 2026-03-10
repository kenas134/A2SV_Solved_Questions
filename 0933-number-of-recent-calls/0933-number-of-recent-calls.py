class RecentCounter:

    def __init__(self):
        self.d = []    

    def ping(self, t: int) -> int:
        count = 0
        self.d.append(t)
        for num in reversed(self.d):
            if num >= t - 3000 and num <= t:
                count += 1
            else:
                return count
        return count 


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)