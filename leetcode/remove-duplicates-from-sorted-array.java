//https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import java.util.HashSet;

class Solution {
    public int removeDuplicates(int[] nums) {
        HashSet<Integer> unique = new HashSet<Integer>();
        int index = 0;
        for(int i:nums){
            if(!unique.contains(i)){
                nums[index++] = i;
            }
            unique.add(i);
        }
        return unique.size();
    }
}
