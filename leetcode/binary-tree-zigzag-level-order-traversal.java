// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

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

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<List<Integer>>();
        
        if(root == null) return out;
        
        Stack<TreeNode> even = new Stack<TreeNode>();
        Stack<TreeNode> odd = new Stack<TreeNode>();
        
        even.push(root);
        ArrayList<Integer> currLevel;
                
        while(!even.isEmpty() || !odd.isEmpty()){
            currLevel = new ArrayList<Integer>();
            
            while(!even.isEmpty()){
                TreeNode temp = even.pop();
                if(temp != null){
                    odd.push(temp.left);
                    odd.push(temp.right);
                    currLevel.add(temp.val);
                }
            }
            if(!currLevel.isEmpty()) out.add(currLevel);
            
            currLevel = new ArrayList<Integer>();
            
            while(!odd.isEmpty()){
                TreeNode temp = odd.pop();
                if(temp != null){
                    even.push(temp.right);
                    even.push(temp.left);
                    currLevel.add(temp.val);
                }
            }
            if(!currLevel.isEmpty()) out.add(currLevel);
        }
        
        return out;
    }
}