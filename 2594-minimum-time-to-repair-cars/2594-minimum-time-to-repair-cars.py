class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = min(ranks) * cars**2
        ans = inf
        while l<=r:
            mid = l + (r - l)//2
            if self.can_repair(cars,ranks,mid):
                r = mid - 1
                ans = min(ans,mid)
            else:
                l = mid + 1
        return ans
    def can_repair(self,cars,ranks,time):
        repaired_cars= 0
        for r in ranks:
            repaired_cars += int(sqrt(time//r))
        if repaired_cars >= cars:
            return True
        return False