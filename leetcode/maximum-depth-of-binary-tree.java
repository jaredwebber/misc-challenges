//https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution {
    // Provided TreeNode class
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

    public int maxDepth(TreeNode root) {
        return searchMax(root, 0);
    }
    
    private int searchMax(TreeNode curr, int depth){
        if(curr != null){
            int max = Math.max(searchMax(curr.left, depth+1), searchMax(curr.right, depth+1));
            return max;
        }
        return depth;
    }
}
