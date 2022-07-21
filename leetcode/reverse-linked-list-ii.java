// https://leetcode.com/problems/reverse-linked-list-ii/

class Solution {

	public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
		ListNode(int val) { this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right || head == null || head.next == null) return head;
        
        ListNode startReverse = head;
        ListNode preReverse = null;
        int counter = 1;
        
        while(startReverse != null && counter < left){
            preReverse = startReverse;
            startReverse = startReverse.next;
            counter++;
        }
        
        ListNode curr = startReverse;
        ListNode prev = null;
        
        while(counter <= right && curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            counter++;
        }
              
        if(preReverse != null) preReverse.next = prev;
        else head.next = curr;
        
        if(startReverse == head) return prev;
        
        startReverse.next = curr;      
        
        return head;
    }
}
