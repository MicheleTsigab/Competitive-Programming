class Solution {
    public long maximumOr(int[] nums, int k) {
        long[][] memo = new long[nums.length+1][k+1];
        for (int i = 0; i <= nums.length; i++) {
            for (int j = 0; j <= k; j++) {
                memo[i][j] = -1;
            }
        }
        return search(0, k, nums, memo);
        
    }

    public static long search(int i, int k, int[] nums, long[][] memo) {

        if (i == nums.length) {
            return 0;
        }
        if (memo[i][k] != -1) {
            return memo[i][k];
        }
        long alt = 0;
        for (int x = 0; x <= k; x++) {
            alt = Math.max(alt, (cal(x) * nums[i]) | search(i+1, k-x, nums, memo));
        }
        memo[i][k] = alt;
        return alt;
    }
    public static long cal(int p){
        long val = 1L;
        while(p>0){
            val*=(2L);
            p--;
        }
        return val;
    }

}