class Solution:
    def addDigits(self, num: int) -> int:
        num =str(num)
        while int(num) > 9:
            num = str(sum(int(i) for i in num))
        return int(num)