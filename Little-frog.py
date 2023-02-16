def solve():
    n=int(input())
    nums=[i for i in range(1,n+1)]
    nums.sort()
    l = 0
    r =len(nums) -1 
    ans = []
    while l<r:
        ans.append(nums[l])
        ans.append(nums[r])
        
        l+=1
        r-=1
    if len(ans) < len(nums):
        ans.append(nums[l])
    
    print(*ans)
solve()
#https://codeforces.com/problemset/problem/53/C
