// https://leetcode.com/problems/merge-in-between-linked-lists

class Solution {
    // Provided ListNode class
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode head = list1;
        ListNode startTwo = null;
        ListNode endTwo = null;

        for(int i = 0;i<a-1; i++){
            list1 = list1.next;
        }
        startTwo = list1;

        for(int i = 0; i<= b-a; i++){
            list1 = list1.next;
        }
        endTwo = list1.next;

        startTwo.next = list2;

        while(list2.next != null){
            list2 = list2.next;
        }

        list2.next = endTwo;

        return head;
    }
}
