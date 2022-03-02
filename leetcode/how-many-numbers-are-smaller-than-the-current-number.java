//https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

/* Slow + Inefficient, still O(n) */
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        ArrayList<Integer> sorted = new ArrayList<Integer>();
        for(int i:nums) sorted.add(i);
        Collections.sort(sorted);
      
        for(int i = 0; i<nums.length; i++){
            nums[i] = sorted.indexOf(nums[i]);
        }
        return nums;
    }
}