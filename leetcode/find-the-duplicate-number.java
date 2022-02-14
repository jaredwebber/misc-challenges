//https://leetcode.com/problems/find-the-duplicate-number/

class Solution {
    public int findDuplicate(int[] nums) {
        int[] seen = new int[nums.length];
        for(int i: nums){
            if(seen[i] == 1) return i;
            else seen[i] = 1;
        }
        return -1;
    }
}
