//https://leetcode.com/problems/remove-linked-list-elements/

class Solution {
    //Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode removeElements(ListNode head, int val) {
        while(head!=null && head.val == val) head = head.next;
        ListNode one = head;
        ListNode two = head;
        if(head!=null) two = head.next;
        
        while(one!=null && two!=null){  
            if(two.val != val){
                one.next = two;
                one = one.next;
                two = two.next;
            }else{
                two = two.next;
            }
        }  
        if(one!=null) one.next = two;
        
        return head;
    }
}
