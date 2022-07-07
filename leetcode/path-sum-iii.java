// https://leetcode.com/problems/path-sum-iii/

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

	public int pathSum(TreeNode root, int targetSum) {
        if(root == null) return 0;
        
        int[] paths = new int[1];
        subtree(root, targetSum, paths);
        return paths[0];
    }
    
    // Find sum of each subtree
    private void subtree(TreeNode curr, int target, int[] counter){
        if(curr == null) return;
        sum(curr, target, 0, counter);
        // Get next subtree
        subtree(curr.left, target, counter);
        subtree(curr.right, target, counter);
    }
    
    // Find sum of each path in tree
    private void sum(TreeNode curr, int target, int sum, int[] counter){
        if(curr != null){
            sum+=curr.val;
            if(sum == target) counter[0]++;
            sum(curr.left, target, sum, counter);
            sum(curr.right, target, sum, counter);
        }
    }
}
