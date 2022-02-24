//https://leetcode.com/problems/find-all-duplicates-in-an-array/

/* Slightly more efficient version */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        ArrayList<Integer> twice = new ArrayList<Integer>();
        Arrays.sort(nums);
        for(int i = 0; i< nums.length-1; i++){
            if(nums[i]==nums[i+1]){
                twice.add(nums[i]);
                i++;
            }
        }
        return twice;
    }
}

/* HashMap solution below */
/*
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        ArrayList<Integer> twice = new ArrayList<Integer>();
        HashSet<Integer> seen = new HashSet<Integer>();
        for(int i: nums){
            if(seen.contains(i)) twice.add(i);
            else seen.add(i);
        }
        return twice;
    }
}
*/
