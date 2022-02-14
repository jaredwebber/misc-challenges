//https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution {
    //Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        
        ListNode curr = head;
        ListNode next = head;
        if(next!=null) next = next.next;
        while(curr!=null && next!=null){
            if(curr.val!=next.val){
                curr.next = next;
                curr = curr.next;
                next = next.next;
            }else{
                next = next.next;
            }
        }   
        curr.next = next;
        return head;
    }

}
