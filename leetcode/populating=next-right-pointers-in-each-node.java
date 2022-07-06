// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

import java.util.Deque;
import java.util.LinkedList;

class Solution {

	// Provided Node class
	class Node {
		public int val;
		public Node left;
		public Node right;
		public Node next;
	
		public Node() {}
		
		public Node(int _val) {
			val = _val;
		}
	
		public Node(int _val, Node _left, Node _right, Node _next) {
			val = _val;
			left = _left;
			right = _right;
			next = _next;
		}
	}

    public Node connect(Node root) {
        if(root == null) return null;
        
        Deque<Node> q = new LinkedList<Node>();
      	Node lastSeen = null;
      	int countLevel = 0;
      	int levelCount = 1;
      
      	q.add(root);
      
      	while(!q.isEmpty()){
          	Node curr = q.pop();
          	countLevel++;
          
            curr.next = lastSeen;
            if(countLevel ==  levelCount){
                levelCount = countLevel*2;
                countLevel = 0;
                lastSeen = null;
            }else lastSeen = curr;	

            if(curr.right != null){
                q.add(curr.right);
                q.add(curr.left); 
            }
        }      
      	
        return root;
    }
}