//https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.*;

class Solution {
    // O(n) Approach
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> values = new HashSet<Integer>();
        int maxStreak = 0;
        
        for(int i = 0; i<nums.length; i++) values.add(nums[i]);
        
        for(int i = 0; i<nums.length; i++){
            int currVal = nums[i];
            int currStreak = 1;
            
            // smaller than currVal
            while(values.contains(--currVal)){
                currStreak++;
                values.remove(currVal);
            }
            
            currVal = nums[i];
            
            // bigger than currVal
            while(values.contains(++currVal)){
                currStreak++;
                values.remove(currVal);
            }
            
            maxStreak = Math.max(maxStreak, currStreak);
        }
        
        return maxStreak;
    }

    // O(nlogn) sorting approach
    public int longestConsecutive_NlogN(int[] nums) {
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
