// https://leetcode.com/problems/reverse-linked-list/


//Given Node Class
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) return head;
        
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = curr;
        while(curr!=null){
            next = next.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;     
    }
}