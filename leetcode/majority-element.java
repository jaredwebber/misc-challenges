//https://leetcode.com/problems/majority-element/
import java.util.HashMap;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        for(int i:nums){
            if(seen.containsKey(Integer.valueOf(i))) seen.put(i, seen.get(i)+1);
            else seen.put(i,1);
            if(seen.get(Integer.valueOf(i))>nums.length/2) return i;  
        }
        return -1;
    }
}
