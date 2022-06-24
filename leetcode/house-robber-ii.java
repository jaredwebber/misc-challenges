// https://leetcode.com/problems/house-robber-ii/

class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length];
        int max = 0;
        
        if(nums.length == 1) return nums[0];
        
        for(int i = 0; i<nums.length-1; i++){
            dp[i] = nums[i];
            if(i>2){
                dp[i] += Math.max(dp[i-2], dp[i-3]);
            }else if(i > 1){
                dp[i] += dp[i-2];
            }
            max = Math.max(max, dp[i]);
        }
                
        dp[0] = 0;
        for(int i = 1; i<nums.length; i++){
            dp[i] = nums[i];
            if(i>2){
                dp[i] += Math.max(dp[i-2], dp[i-3]);
            }else if(i > 1){
                dp[i] += dp[i-2];
            }
            max = Math.max(max, dp[i]);
        }
        
        return max;
    }
}
