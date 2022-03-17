//https://leetcode.com/problems/binary-tree-level-order-traversal/

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ordered = new ArrayList<>();
        if(root == null) return ordered;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        
        while(queue.size() > 0){
            List<Integer> level = new ArrayList<Integer>();
            int size = queue.size();
            
            for(int i = 0; i<size; i++){
                TreeNode curr = queue.poll();
                level.add(curr.val);
                if(curr.left != null) queue.add(curr.left);
                if(curr.right != null) queue.add(curr.right);
            }
            ordered.add(level);
        }
        
        return ordered;        
    }
}
