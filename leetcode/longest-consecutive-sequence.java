//https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.Arrays;

class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        int max = 1;
        int curr = 1;
        Arrays.sort(nums);

        for(int i = 0; i<nums.length-1; i++){
            if(nums[i]+1 == nums[i+1]){
                curr++;
            }else if(nums[i] != nums[i+1]){
                max = Math.max(max, curr);
                curr = 1;
            }
        }
        return Math.max(max, curr);
    }
}
