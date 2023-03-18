class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = 0
        self.st = [homepage]

    def visit(self, url: str) -> None:
        while self.st[self.cur]!=self.st[-1]:
            self.st.pop()
        self.st.append(url)
        self.cur +=1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.st[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.st)-1,steps + self.cur)
        return self.st[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)