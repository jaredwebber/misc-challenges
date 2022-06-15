//https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution {
    public String firstPalindrome(String[] words) {
        for(String i:words){
            for(int j = 0; j<i.length()/2 && !i.isEmpty(); j++){
                if(i.charAt(j) != i.charAt(i.length()-1-j)) i = "";
            }
            if(!i.isEmpty()) return i;
        }
        return "";
    }
}
