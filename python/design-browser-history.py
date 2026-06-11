class BrowserHistory:
    class PageTree:
        def __init__(self, url: str, prev: PageTree = None, next: PageTree = None):
            self.url = url
            self.prev = prev
            self.next = next
    
    def __init__(self, homepage: str):
        self.curr = self.PageTree(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = self.PageTree(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
