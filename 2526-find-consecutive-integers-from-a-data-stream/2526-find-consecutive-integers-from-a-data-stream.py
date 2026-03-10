class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.val = value
        self.queue = deque()
        

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.queue.append(num)
            if len(self.queue) >= self.k:
                return True
            else:
                return False
        else:
            self.queue.clear()
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)