// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution {
    public int minimumDeletions(int[] nums) {
        
        if(nums.length < 3) return nums.length;
        
        int[] min = new int[]{Integer.MAX_VALUE, -1};
        int[] max = new int[]{Integer.MIN_VALUE, -1};
        for(int i = 0; i<nums.length; i++){
            if(nums[i] < min[0]){
                min[0] = nums[i];
                min[1] = i;
            }
            if(nums[i] > max[0]){
                max[0] = nums[i];
                max[1] = i;
            }
        }
        
        // 3 Minimum Options
        // 1. (left + 1) + (n - right)
        // 2. (right + 1)
        // 3. (n - left)
        if(max[1] > min[1]) return Math.min(Math.min(min[1]+1 + nums.length-max[1], max[1]+1), nums.length-min[1]);
        return Math.min(Math.min(max[1]+1 + nums.length-min[1], min[1]+1), nums.length-max[1]);
    }
}