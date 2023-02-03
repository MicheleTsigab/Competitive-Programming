class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, m = divmod(sum(nums), k)
        if m: return False
        dp, n = [0]*k, len(nums)
        nums.sort(reverse=True)
        def dfs(i):
            if i == n:
                return len(set(dp)) == 1
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and dfs(i+1):
                    return True
                dp[j] -= nums[i]
                if not dp[j]: break
            return False
        return nums[0] <= target and dfs(0)
            