// https://leetcode.com/problems/balance-a-binary-search-tree/

import java.util.ArrayList;
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

	public TreeNode balanceBST(TreeNode root) {       
		ArrayList<Integer> values = new ArrayList<Integer>();
		inOrderTraversal(root, values);
			
		int mid = values.size()/2;
		root = new TreeNode(values.get(mid));

		buildTree(root, values, 0, mid-1);// left subtree
		buildTree(root, values, mid+1, values.size()-1); // right subtree
		
		return root;
	}
	
	private void buildTree(TreeNode node, List<Integer> values, int left, int right){
		if(left <= right){
			int val = values.get(left + (right-left)/2);
			int mid = (left + (right-left)/2);
			if(node.val > val){
				node.left = new TreeNode(val);
				buildTree(node.left, values, left, mid-1);
				buildTree(node.left, values, mid+1, right);
			}else{
				node.right = new TreeNode(val);
				buildTree(node.right, values, left, mid-1);
				buildTree(node.right, values, mid+1, right);
			}
		}
	}
	
	private void inOrderTraversal(TreeNode node, List<Integer> values){
		if(node != null){
			inOrderTraversal(node.left, values);
			values.add(node.val);
			inOrderTraversal(node.right, values);
		}
	}
}
