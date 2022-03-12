//https://leetcode.com/problems/maximum-binary-tree/

import java.util.Arrays;

class Solution {

    //provided treenode class
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

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums.length == 1) return new TreeNode(nums[0]);
        
        int maxIndex = 0;
        int maxValue = nums[0];
        for(int i= 1; i<nums.length; i++){
            if(nums[i]>maxValue){
                maxValue = nums[i];
                maxIndex = i;
            }
        }
        
        TreeNode node = new TreeNode(nums[maxIndex]);
        if(maxIndex>0) node.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums, 0, maxIndex));
        if(maxIndex<nums.length-1) node.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, maxIndex+1, nums.length));
        
        return node;
    }
}