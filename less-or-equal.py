def solve():
    n,k=[int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    nums.sort()
    if k==0:
        if nums[0]==1:
            print(-1)
        else:
            print(1)
    elif k!=len(nums):
        if nums[k-1]!=nums[k]:
            print(nums[k-1])
        else: 
            print(-1)
    else:
        print(nums[k-1])
        
            
solve()
