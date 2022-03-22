//https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        ArrayList<Integer> missing = new ArrayList<Integer>();
        int[] allValues = new int[nums.length+1];
        for(int i = 0; i<nums.length; i++){
            allValues[nums[i]] = 1;
        }
                
        for(int i = 1; i<allValues.length; i++){
            if(allValues[i]==0) missing.add(i);
        }
        
        return missing;
    }
}