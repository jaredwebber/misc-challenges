//https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class Solution {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        return traverse(cloned, target, null);
    }
    
    private TreeNode traverse(TreeNode curr, TreeNode target, TreeNode match){      
        if(curr != null){
            if(curr.val == target.val) match = curr;
            else{
                match = traverse(curr.left, target, match);
                match = traverse(curr.right, target, match);
            }
        }
        return match;
    }
}
