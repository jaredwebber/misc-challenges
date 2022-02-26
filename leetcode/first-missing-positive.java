//https://leetcode.com/problems/first-missing-positive/

import java.util.Arrays;

class Solution {
    public int firstMissingPositive(int[] nums) {
        int curr = 0;
        
        Arrays.sort(nums);
        
        for(int i:nums){
            if(i == curr+1){
                curr++;
            }
        }
        
        if(curr == 0) return 1;
        
        return curr+1;    
    }
}