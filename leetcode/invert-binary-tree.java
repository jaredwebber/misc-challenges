// https://leetcode.com/problems/invert-binary-tree/

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

    public TreeNode invertTree(TreeNode root) {
        if(root != null && (root.left != null || root.right != null)){
            TreeNode newRight = root.left;
            root.left = root.right;
            root.right = newRight;
            invertTree(root.left);
            invertTree(root.right);
        }
        return root;
    }
}
