//https://leetcode.com/problems/linked-list-cycle/

//given Node class
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

//Non-Destructive Approach
class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head == null || head.next == null) return false;

        ListNode slow = head;
        ListNode fast = head.next;
        
        while(!slow.equals(fast)){
            if(slow == null || fast == null) return false;
            slow = slow.next;
            fast = fast.next;
            if(fast != null) fast = fast.next;
        }
        return true;
    }
}

// Destructive Approach
/*
class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null || head.next == null) return false;
        
        while(head != null && head.val != Integer.MAX_VALUE){
            head.val = Integer.MAX_VALUE;
            head = head.next;
        }
        if(head == null) return false;
        return true;
    }
}
*/