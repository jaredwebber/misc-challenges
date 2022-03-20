//https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution {
    public int findMin(int[] nums) {
        int hi = nums.length-1;
        int lo = 0;
        int mid = (hi+lo)/2;
        
        //array is not rotated
        if(nums[lo] < nums[hi]) return nums[lo];

        while(lo < hi){
            if(mid>0 && nums[mid] < nums[mid-1]) return nums[mid];
            
            if(nums[mid] < nums[hi]) hi = mid-1;
            else lo = mid+1;
            
            mid = lo+((hi-lo)/2);
        }
        
        return nums[lo];
    }
}
