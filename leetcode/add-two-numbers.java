// https://leetcode.com/problems/add-two-numbers/

class Solution {

	// Provided ListNode class
	public class ListNode {
		int val;
		ListNode next;
		ListNode() {}
		ListNode(int val) { this.val = val; }
		ListNode(int val, ListNode next) { this.val = val; this.next = next; }
	}

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode combined = new ListNode();
        ListNode curr = combined;
        int carry = 0;
        
        while(l1 != null || l2 != null){
            int sum = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + carry;
            if(sum > 9){
                sum = sum%10;
                carry = 1;
            }else{
                carry = 0;
            }
            
            curr.val = sum;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
            if(l1 != null || l2 != null){
                ListNode next = new ListNode();
                curr.next = next;
                curr = curr.next;
            }
        }
        
        if(carry == 1){
            curr.next = new ListNode(1);
        }
        
        return combined;
    }
}
