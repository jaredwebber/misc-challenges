//https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 2) return s;

        int[] interval = new int[2];
        
        for(int i = 0; i<s.length()-1; i++){
            extendPalindrome(s, i, i, interval);//odd length palindromes
            extendPalindrome(s, i, i+1, interval);//even length palindromes
        }
        return s.substring(interval[0], interval[1]+1);
    }
    
    private void extendPalindrome(String s, int start, int end, int[] interval){
        while(start>=0 && end<s.length() && s.charAt(start) == s.charAt(end)){
            start--;
            end++;
        }    

        if((end-1)-(start+1) > (interval[1] - interval[0])){
            interval[0] = start+1;
            interval[1] = end-1;
        }
        
    }
}
