//https://leetcode.com/problems/validate-binary-search-tree/

class Solution {

    //Provided TreeNode
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

    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean validate(TreeNode curr, long min, long max){
        if(curr == null) return true;
        if(curr.val <= min || curr.val >= max) return false;
        
        return validate(curr.left, min, curr.val) &&
            validate(curr.right, curr.val, max);
    }
}
/* HashSet Approach
class Solution {
    public boolean isValidBST(TreeNode root) {
        HashSet<Integer> seenValues = new HashSet<Integer>();
        seenValues.add(root.val);
        
        return traverse(root.left, seenValues, Integer.MIN_VALUE, root.val) &&
                traverse(root.right, seenValues, root.val, Integer.MAX_VALUE);
    }
    
    private boolean traverse(TreeNode curr, HashSet<Integer> seenValues, int min, int max){
        if(curr == null) return true;
        if(curr.val < min || curr.val > max || seenValues.contains(curr.val)) return false;
        
        seenValues.add(curr.val);
        return traverse(curr.left, seenValues, min, curr.val) &&
            traverse(curr.right, seenValues, curr.val, max);
    }
}
*/