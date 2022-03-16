//https://leetcode.com/problems/copy-list-with-random-pointer/

import java.util.HashMap;

class Solution {

    class Node {
        int val;
        Node next;
        Node random;
    
        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    public Node copyRandomList(Node head) {   
        HashMap<Node, Node> map = new HashMap<Node, Node>();
        if(head == null) return null;
        
        Node curr = head;
        while(curr!=null){
            map.put(curr, new Node(curr.val));
            curr = curr.next;
        }
        curr = head;
        while(curr!=null){
            Node tmp = map.get(curr);
            tmp.next = map.get(curr.next);
            tmp.random = map.get(curr.random);
            map.put(curr, tmp);
            curr = curr.next;
        }
        
        return map.get(head);
    }
}