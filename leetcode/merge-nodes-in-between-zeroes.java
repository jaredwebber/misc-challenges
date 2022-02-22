//https://leetcode.com/problems/merge-nodes-in-between-zeros/

class Solution {

    //Linked List Node provided
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode mergeNodes(ListNode head) {
        ListNode curr = new ListNode();
        ListNode newHead = new ListNode(0, curr);
        int currSum = 0;
        head = head.next;
        
        while(head!=null){
            if(head.val != 0){
                currSum+=head.val;
            }else{
                if(curr.next == null){
                    ListNode next = null;
                    if(head.next != null) next = new ListNode();
                    curr.val = currSum;
                    curr.next = next;
                    curr = next;
                    currSum = 0;
                }
            }
            head = head.next;
        }
        
        return newHead.next;
    }
}