// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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

    public List<Integer> getAllElementsBruteForce(TreeNode root1, TreeNode root2) {
        List<Integer> list = new ArrayList<Integer>();
        
        getAll(root1, list);
        getAll(root2, list);

        Collections.sort(list);
        
        return list;
    }
    
    private void getAll(TreeNode node, List<Integer> list){
        if(node!=null){
            list.add(node.val);
            getAll(node.left, list);
            getAll(node.right, list);
        }
    }
}