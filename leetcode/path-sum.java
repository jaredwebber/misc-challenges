//https://leetcode.com/problems/path-sum/

class Solution {

    //provided treenode class
    class TreeNode {
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

    public boolean hasPathSum(TreeNode root, int targetSum) {
        return search(root, 0, targetSum);
    }
    
    private boolean search(TreeNode curr, int currSum, int targetSum){
        if(curr == null) return false;
        if(curr.left==null && curr.right==null && currSum+curr.val == targetSum) return true;
        
        return search(curr.left, currSum+curr.val, targetSum) ||
            search(curr.right, currSum+curr.val, targetSum);
    }
}