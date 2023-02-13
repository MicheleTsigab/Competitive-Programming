for _ in range(int(input())):
    #n,k =[ int(i) forinput().split()]gb
    n = int(input())
    nums = list(map(int, input().split()))
    seeker,slow = 0,0
    total = 0
    while slow < len(nums):
        num = nums[slow]
        mx = num
        seeker = slow
        while seeker < n and ((num < 0 and nums[seeker] < 0) or (num > 0 and nums[seeker] > 0)):
            mx = max(mx, nums[seeker])
            seeker += 1
        total += mx
        slow = seeker
    print(total)
