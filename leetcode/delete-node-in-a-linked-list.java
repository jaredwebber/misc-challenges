//https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution {

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public void deleteNode(ListNode node) {
        ListNode curr = node.next;
        while(curr!=null){
            node.val = curr.val;
            node.next = curr.next;
            node = node.next;
            curr = curr.next;
        }
    }
}
