//https://leetcode.com/problems/maximum-erasure-value/

import java.util.HashMap;

class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int left = 0;
        int currSub = 0;
        int maxSub = 0;
        HashMap<Integer, Integer> sub = new HashMap<Integer, Integer>();
        
        for(int i = 0; i<nums.length; i++){
            currSub+=nums[i];
            if(sub.get(nums[i]) != null){
                while(left <= sub.get(nums[i])){
                    currSub -= nums[left++];
                }
            }
            sub.put(nums[i], i);
            maxSub = Math.max(currSub, maxSub);
        }
        
        return maxSub;
    }
}
