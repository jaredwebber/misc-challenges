//https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import java.util.HashSet;

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

    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> seen = new HashSet<Integer>();
        return search(root, seen, k);
    }
    
    private boolean search(TreeNode curr, HashSet<Integer> seen, int k){
        if(curr != null) {
            int need = k - curr.val;
            if(seen.contains(need)) return true;
            seen.add(curr.val);
            
            return search(curr.left, seen, k) || search(curr.right, seen, k);
        }
        return false;  
    }
}
