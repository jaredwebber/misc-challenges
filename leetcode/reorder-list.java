//https://leetcode.com/problems/reorder-list/

import java.util.HashMap;

class Solution {
	// Provided ListNode class
	public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
		ListNode(int val) { this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

	/*
	 * Should split list into 2
	 * Reverse 'last-half' list
	 * Merge first list alternating with reversed 2nd list
	 */

	// Inefficient Space & Time Solution
    public void reorderList(ListNode head) {
        HashMap<Integer, ListNode> nodePos = new HashMap<Integer, ListNode>();
        int count = 0;
        ListNode curr = head;
        
        while(curr != null){
            nodePos.put(count++, curr);
            curr = curr.next;
        }
        
        for(int i = 0; i<(count+1)/2; i++){
            nodePos.get(i).next = nodePos.get(count-1-i);
            nodePos.get(count-1-i).next = nodePos.get(i+1);
        }
        nodePos.get(count/2).next = null;
    }
}
