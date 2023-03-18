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
        while steps and self.cur:
            steps -=1
            self.cur-=1
        return self.st[self.cur]

    def forward(self, steps: int) -> str:
        while steps and self.cur < len(self.st) - 1:
            steps-=1
            self.cur+=1
        return self.st[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)