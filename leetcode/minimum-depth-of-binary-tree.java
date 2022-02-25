//https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution {
    //provided node class
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

    public int minDepth(TreeNode root) {
        return root!=null ? search(root, 1) : 0;
    }
    
    private int search(TreeNode curr, int depth){
        if(curr == null) return Integer.MAX_VALUE;
        if(curr.left==null && curr.right == null) return depth;
        
        return Math.min(search(curr.left, depth+1), search(curr.right, depth+1));
    }
}
