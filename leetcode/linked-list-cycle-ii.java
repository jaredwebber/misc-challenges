// https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=study-plan&id=level-1

import java.util.HashSet;

class Solution {
    // Provided ListNode class
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> map = new HashSet<ListNode>();

        while(head != null){
            if(map.contains(head)) return head;
            map.add(head);
            head = head.next;
        }

        return null;
    }
}
