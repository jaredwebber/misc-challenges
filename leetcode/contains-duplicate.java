import java.util.HashMap;

//https://leetcode.com/problems/contains-duplicate/

class Solution {
    //Hashmap worked faster than ArrayList even though theres no value pairing
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        for(int i = 0; i<nums.length; i++){
            if(counter.containsKey(nums[i])) return true;
            counter.put(nums[i], 0);
        }
        return false;
    }
}