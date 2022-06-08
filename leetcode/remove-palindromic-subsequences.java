//https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution {
    public int removePalindromeSub(String s) {
        // Since input is limited to 'a' and 'b' there are 
        // max 2 steps to remove all subsequences, since all 'a's
        // could be removed, followed by all 'b's
        char[] arr = s.toCharArray();
        for(int i = 0; i<arr.length/2; i++){
            if(arr[i] != arr[arr.length-1-i]) return 2;
        }
        return 1;
    }    
}