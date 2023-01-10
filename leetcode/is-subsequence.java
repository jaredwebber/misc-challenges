// https://leetcode.com/problems/is-subsequence/description

class Solution {
    public boolean isSubsequence(String s, String t) {
        char[] one = s.toCharArray();
        char[] two = t.toCharArray();
        int currIndex = 0;

        if(one.length == 0) return true;
        if(two.length == 0) return false;

        for(int i = 0; i<two.length; i++){
            if(two[i] == one[currIndex]){
                currIndex++;
                if(currIndex == one.length) return true;
            }
        }

        return currIndex == one.length;
    }
}