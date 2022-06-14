//https://leetcode.com/problems/same-tree/

class Solution {

	// Provided TreeNode class
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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        return isSame(p,q);
    }
    
    private boolean isSame(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        else if(p == null || q == null) return false;
        else if(p.val != q.val) return false;
        
        return isSame(p.left, q.left) && isSame(p.right, q.right);
    }
}
