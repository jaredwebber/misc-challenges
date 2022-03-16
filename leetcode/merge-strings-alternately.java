//https://leetcode.com/problems/merge-strings-alternately/

class Solution {
    public String mergeAlternately(String word1, String word2) {
        String sol = "";
        int one = word1.length();
        int two = word2.length();
        for(int i = 0; i<Math.max(one,two); i++){
            if(i<one) sol+=word1.charAt(i);
            if(i<two) sol+=word2.charAt(i);
        }
        return sol;
    }
}
