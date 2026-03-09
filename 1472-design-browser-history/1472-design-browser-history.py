class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.prev = None
        self.cur = self.head


    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = self.cur.next

        

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.prev:
            self.cur = self.cur.prev
            i += 1

        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.next:
            self.cur = self.cur.next
            i += 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)