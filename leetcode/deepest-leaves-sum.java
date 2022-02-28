//https://leetcode.com/problems/deepest-leaves-sum/

import java.util.HashMap;

class Solution {

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

    public int deepestLeavesSum(TreeNode root) {
        if(root.left == null && root.right == null) return root.val;
        HashMap<Integer, Integer> depthSums = new HashMap<Integer, Integer>();
        return depthSums.get(traverse(root, 0, depthSums, 0));        
    }
    
    private int traverse(TreeNode curr, int depth, HashMap<Integer, Integer> depthSums, int maxDepth){
        if(curr == null) return 0;
        if(curr.left == null && curr.right == null){
            if(depthSums.get(depth)!=null){
                depthSums.put(depth, depthSums.get(depth)+curr.val);
            }else depthSums.put(depth, curr.val);
        }

        maxDepth = Math.max(depth, maxDepth);
        maxDepth = Math.max(traverse(curr.left, depth+1, depthSums, maxDepth), maxDepth);
        maxDepth = Math.max(traverse(curr.right, depth+1, depthSums, maxDepth), maxDepth);
          
        return maxDepth;
    }
}