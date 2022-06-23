//https://leetcode.com/problems/contains-duplicate/

import java.util.HashMap;
import java.util.HashSet;

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

    //Similiar Runtime as above
    public boolean containsDuplicateSet(int[] nums) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for(int i = 0; i<nums.length; i++){
            if(seen.contains(nums[i])) return true;
            seen.add(nums[i]);
        }
        return false;
    }
}