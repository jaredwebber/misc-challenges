//https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length-1;
        int mid = hi/2;
        
        while(lo<hi){
            if(nums[mid] == target) return mid;
            
            if(nums[lo] <= nums[mid]){
                if(target >= nums[lo] && target<nums[mid]) hi = mid-1;
                else lo = mid+1;
            }else{
                if(target >= nums[lo] || target<nums[mid]) hi = mid-1;
                else lo = mid+1;
            }
                
            mid = lo + (hi-lo)/2;
        }
        return nums[lo] == target ? lo : -1;
    }
}