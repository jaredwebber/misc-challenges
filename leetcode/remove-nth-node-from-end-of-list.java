//https://leetcode.com/problems/remove-nth-node-from-end-of-list/

import java.util.HashMap;

class Solution {

    //Provided Node class
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        HashMap<Integer, ListNode> mapping = new HashMap<Integer, ListNode>();
        ListNode curr = head;
        int index = 0;
        
        if(head == null || head.next == null) return null;
        
        while(curr != null){
            mapping.put(index++, curr);
            curr = curr.next;
        }

        if(index == n){
            head = head.next; 
        }else{
            mapping.get(index-n-1).next = mapping.get(index-n+1);
        }
        
        return head;
    }
}
