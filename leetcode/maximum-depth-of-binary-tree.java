//https://leetcode.com/problems/maximum-depth-of-binary-tree/

/* Two Different Approaches */

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

    public int maxDepth(TreeNode root) {
        return root!=null ? search(root, 1) : 0;
    }
    
    private int search(TreeNode curr, int depth){
        if(curr == null) return Integer.MIN_VALUE;
        if(curr.left == null && curr.right == null) return depth;
        
        return Math.max(search(curr.left, depth+1), search(curr.right, depth+1));
    }
}

/*
class Solution {
    public int maxDepth(TreeNode root) {
        if(root==null) return 0;
        return depth(root)+1;
    }
    
    private int depth(TreeNode node){
        int left = 0;
        int right = 0;
        
        if(node!=null){
            if(node.left!=null){
                left++;
            }
            if(node.right!=null){
                right++;
            }
            left+=depth(node.left);
            right+=depth(node.right);
        }
        return Math.max(right,left);
    }
}
*/