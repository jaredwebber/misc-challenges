//https://leetcode.com/problems/binary-search/

class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        
        while(left <= right){
            // Emulated 'mid' pointer for slight space efficiency increase
            if(nums[(left+right)/2] == target) return (left+right)/2;
            else if(nums[(left+right)/2] > target) right = ((left+right)/2)-1;
            else left = ((left+right)/2)+1;
        }
        
        return -1;
    }
}