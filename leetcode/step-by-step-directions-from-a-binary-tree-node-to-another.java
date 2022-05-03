//https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

// Memory Allocation Exceeded
class Solution {

    //Provided TreeNode Class
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
    
    public String getDirections(TreeNode root, int start, int dest)
    {
        String[] paths = new String[]{"", ""};
        traverse(root, start, dest, new StringBuilder(), paths);
        int count = 0;

        for(int i = 0; i < Math.min(paths[0].length(), paths[1].length()); i++){
            if(paths[0].charAt(i) == paths[1].charAt(i)){
                count++;
            }else break;
        }
                
        paths[0] = paths[0].substring(count);
        paths[1] = paths[1].substring(count);
        
        paths[0] = paths[0].replaceAll("L", "U");
        paths[0] = paths[0].replaceAll("R", "U");

        return "U".repeat(paths[0].length())+paths[1];
    }


    private void traverse(TreeNode node, int start, int dest, StringBuilder path, String[] paths)
    {
        if(node != null){
            if(node.val == start){
                paths[0] = path.toString();
            }else if(node.val == dest){
                paths[1] = path.toString();
            }
            if(paths[0].isEmpty() || paths[1].isEmpty()){
                // The need to store the original path for use traversing the right node
                // causes Memory Allocation Exceeded
                    StringBuilder tempPath = new StringBuilder(path);
                    traverse(node.left, start, dest, path.append("L"), paths);
                    traverse(node.right, start, dest, tempPath.append("R"), paths);
            }
        }
    }
}