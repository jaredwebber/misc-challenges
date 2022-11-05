// https://leetcode.com/problems/merge-k-sorted-lists

import java.util.PriorityQueue;

class Solution {

	// Provided ListNode class
	public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
		ListNode(int val) { this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>((a,b)->a.val - b.val);
        for(ListNode i:lists)
            while( i != null){
                queue.add(i);
                i = i.next;
            }
        ListNode head = new ListNode(0, null);
        ListNode curr = head;
        while(!queue.isEmpty()){
            curr.next = queue.poll();
            curr = curr.next;
        }
        curr.next = null;

        return head.next;
    }   
}
