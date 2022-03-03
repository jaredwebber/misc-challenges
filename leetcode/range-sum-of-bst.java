//https://leetcode.com/problems/range-sum-of-bst/

class Solution {

    //Provided node class
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

    public int rangeSumBST(TreeNode root, int low, int high) {
        return search(root, low, high, 0);
    }
    
    private int search(TreeNode curr, int low, int high, int sum){
        if(curr==null) return sum;
        
        if(curr.val>=low && curr.val<=high) sum+=curr.val;
    
        sum = search(curr.left, low, high, sum);
        sum = search(curr.right, low, high, sum);
        
        return sum;
    }
}
