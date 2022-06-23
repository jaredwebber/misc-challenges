// https://leetcode.com/problems/reverse-linked-list/

class Solution {
    //Provided Node Class
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) return head;

        ListNode prev = head;
        ListNode curr = prev.next;
        ListNode next = curr.next;
        
        prev.next = null;
        
        while(curr != null){
            curr.next = prev;
            prev = curr;
            curr = next;
            if(next != null) next = next.next;
        }
        
        return prev;
    }
}
