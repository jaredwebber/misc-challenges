//https://leetcode.com/problems/palindrome-linked-list/

import java.util.ArrayList;
 
class Solution {
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> vals= new ArrayList<Integer>();
        ListNode odd = head.next;
        ListNode even = head;
        while(odd!=null && even!=null){
            if(even!=null){
                vals.add(even.val);
                odd = even.next;  
            }
            if(odd!=null){
                vals.add(odd.val);
                even = odd.next;  
            }
        }
        for(int i = 0; i<vals.size()/2; i++){
            if(vals.get(i)!=vals.get(vals.size()-i-1)) return false;
        }
        return true;    
    }
}
