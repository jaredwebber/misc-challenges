// https://leetcode.com/problems/merge-sorted-array/

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int n1 = m-1;
        int n2 = n-1;
        
        while(n1 >=0 && n2 >= 0){
            nums1[n1+n2+1] = nums1[n1] >= nums2[n2] ? nums1[n1--] : nums2[n2--];
        }
        
        while(n1+n2+1 >= 0){
            nums1[n1+n2+1] = n1 < 0 ? nums2[n2--] : nums1[n1--];
        }
    }
}