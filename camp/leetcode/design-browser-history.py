class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        
        new = ListNode(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:

        while self.curr and self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val


    def forward(self, steps: int) -> str:

        while self.curr and self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)