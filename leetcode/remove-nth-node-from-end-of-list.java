//https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// 2 Node Approach
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
        ListNode fast = head;
        ListNode slow = new ListNode(0, head);
                
        for(int i = 0; i<n; i++){
            fast = fast.next;
        }
        
        while(fast != null){
            slow = slow.next;
            fast = fast.next;
        }
        
        if(slow.next == head) head = head.next;
        else slow.next = slow.next.next;
        
        return head;
    }
}

/* 3 Node Approach
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
        if(head == null) return head;
        
        ListNode start = new ListNode(0, head);
        ListNode fast = head;
        ListNode slow = start;
        
        for(int i = 0; i<n; i++){
            fast = fast.next;
        }

        while(fast!=null){
            fast = fast.next;
            slow = slow.next;
        }
        
        slow.next = slow.next.next;
        
        return start.next;
    }
}
*/

/* Less Space-efficient Approach

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
*/