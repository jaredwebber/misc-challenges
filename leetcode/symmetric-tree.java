//https://leetcode.com/problems/symmetric-tree/

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

    public boolean isSymmetric(TreeNode root) {
        return recurse(root.left, root.right);
    }
    
    private boolean recurse(TreeNode left, TreeNode right){
        if(left == null && right == null) return true;
        else if(left == null || right == null) return false;
        
        return left.val == right.val && recurse(left.left, right.right) && recurse(left.right, right.left);
    }
}
