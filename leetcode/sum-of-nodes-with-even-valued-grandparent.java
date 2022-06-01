//https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

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

	final char LEFT = 'L';
	final char RIGHT = 'R';

    public int sumEvenGrandparent(TreeNode root) {
        int[] sum = new int[1];
        if(root.left != null){
            traverse(root.left.left, root, LEFT, LEFT, sum);
            traverse(root.left.right, root, LEFT, RIGHT, sum);
        }
        if(root.right != null){
            traverse(root.right.left, root, RIGHT, LEFT, sum);
            traverse(root.right.right, root, RIGHT, RIGHT, sum);
        }

        return sum[0];
    }
    
    private void traverse(TreeNode curr, TreeNode grandparent, char gSide, char pSide, int[] sum){
        if(grandparent != null && curr != null){
            if(grandparent.val % 2 == 0) sum[0]+= curr.val;
            
            if(gSide == LEFT){
                traverse(curr.left, grandparent.left, pSide, LEFT, sum);
                traverse(curr.right, grandparent.left, pSide, RIGHT, sum);
            }else{
                traverse(curr.left, grandparent.right, pSide, LEFT, sum);
                traverse(curr.right, grandparent.right, pSide, RIGHT, sum);
            }
        }
    }
}