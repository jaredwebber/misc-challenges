// https://leetcode.com/problems/find-pivot-index/description/

class Solution {
    public int pivotIndex(int[] nums) {
        int leftSum = 0;
        int rightSum = 0;

        for(int i = 1; i<nums.length; i++) rightSum+=nums[i];
        if(rightSum == leftSum) return 0;

        for(int i = 1; i<nums.length; i++){
            rightSum -= nums[i];
            leftSum += nums[i-1];
            if(rightSum == leftSum) return i;
        }

        return -1;
    } 
}
