//https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import java.util.Arrays;

class Solution {
    //Provided TreeNode class
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode root = new TreeNode(nums[nums.length/2]);
        if(nums.length == 1) return root;
        if(nums.length/2 >0) root.left = sortedArrayToBST(Arrays.copyOfRange(nums,0,nums.length/2));
        if(nums.length/2<nums.length-1) root.right = sortedArrayToBST(Arrays.copyOfRange(nums,nums.length/2+1, nums.length));
        return root;
    }
}