//https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

import java.util.Arrays;

class Solution {
    public int minDifference(int[] nums) {
        if(nums.length <= 4) return 0;
        
        Arrays.sort(nums);
    
        // After sort, either switching:
        // 3 of the smallest
        // 3 of the largest
        // 2 small, 1 large
        // 1 small, 2 large        
        
        return Math.min(
            //       3 largest switched             3 smallest switched
            Math.min(nums[nums.length-1] - nums[3], nums[nums.length-4] - nums[0]),
            //       2 large, 1 small               1 large, 2 small 
            Math.min(nums[nums.length-2] - nums[2], nums[nums.length-3] - nums[1])
        );
    }
}