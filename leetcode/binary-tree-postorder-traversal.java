// https://leetcode.com/problems/binary-tree-postorder-traversal/description/

import java.util.*;

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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        traverse(root, list);
        return list;
    }

    private void traverse(TreeNode node, List<Integer> list) {
        if(node != null){
            list.add(node.val);
            traverse(node.left, list);
            traverse(node.right, list);
        }
    }
}

