// https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution {
    // O(n+m) solution - should find O(log(n+m)) approach
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = new int[nums1.length+nums2.length];
        int one = 0;
        int two = 0;
        
        for(int i = 0; i<merged.length; i++){
            if(one < nums1.length && two < nums2.length){
                merged[i] = nums1[one] <= nums2[two] ? nums1[one++] : nums2[two++];
            }else{
                merged[i] = one < nums1.length ? nums1[one++] : nums2[two++];
            }
        }
        
        for(int i = 0; i<merged.length; i++){
            System.out.println(merged[i]);
        }
        
        return merged.length % 2 == 0 ? (double)(merged[merged.length/2]+merged[merged.length/2-1])/2 : merged[merged.length/2];
    }
}
