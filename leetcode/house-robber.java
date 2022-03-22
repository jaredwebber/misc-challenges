//https://leetcode.com/problems/house-robber/

class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1) return nums[0];
        
        int one = 0;
        int two = 0;
        int temp = 0;
        
        for(int i: nums){
            temp = one;
            one = Math.max(two + i, one);
            two = temp;
        }
        
        return Math.max(one, two);
    }
}