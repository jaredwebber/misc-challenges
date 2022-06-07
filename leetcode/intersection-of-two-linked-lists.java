
//https://leetcode.com/problems/intersection-of-two-linked-lists/

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

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> seen = new HashSet<ListNode>();
        
        ListNode a = headA;
        ListNode b = headB;
        
        while(a != null || b!= null){            
            if(a != null){
                if(seen.contains(a)){
                    return a;
                }else{
                    seen.add(a);
                    a = a.next;
                }
            }
            if(b != null){
                if(seen.contains(b)){
                    return b;
                }else{
                    seen.add(b);
                    b = b.next;
                }
            }
        }
        
        return null;
    }
}