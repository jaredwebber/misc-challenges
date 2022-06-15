//https://leetcode.com/problems/search-insert-position/

class Solution {
    public int searchInsert(int[] nums, int target) {       
        int lo = 0;
        int hi = nums.length-1;
        int mid = hi/2;
        
        while(lo <= hi){
            if(nums[mid] == target) return mid;
            else if(nums[mid] < target) lo = mid+1;
            else hi = mid-1;
            
            mid = lo + (hi-lo)/2;
        }
        
        return lo;
    }
}