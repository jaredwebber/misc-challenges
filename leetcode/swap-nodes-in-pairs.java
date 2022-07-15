
// https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution {

	// Provided ListNode class
	public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
		ListNode(int val) { this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode odd = head;
        ListNode even = head.next;
        ListNode oddCurr = odd;
        ListNode evenCurr = even;        
        
        while(evenCurr != null || oddCurr != null){
            if(oddCurr != null) {
                oddCurr.next = oddCurr.next != null ? oddCurr.next.next != null ? oddCurr.next.next : null : null;
                oddCurr = oddCurr.next;
            }
            if(evenCurr != null){
                evenCurr.next = evenCurr.next != null ? evenCurr.next.next != null ? evenCurr.next.next : null : null;
                evenCurr = evenCurr.next;
            }
        }    
        
        head = even;
        even = even.next;
        ListNode curr = head;
        
        while(even != null || odd != null){
            if(even != null && odd != null){
                curr.next = odd;
                odd = odd.next;
                curr = curr.next;
                curr.next = even;
                even = even.next;
                curr = curr.next;
            }else if(even != null){
                curr.next = even;
                even = even.next;
                curr = curr.next;
            }else{
                curr.next = odd;
                odd = odd.next;
                curr = curr.next;
            }
        }
    
        return head;
    }
}