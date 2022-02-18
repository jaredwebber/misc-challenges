//https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    public int balancedStringSplit(String s) {
        int total = 0;
        int count = 0;
        for(int i = 0; i<s.length(); i++){
            count += s.charAt(i) == 'R' ? 1 : -1;
            if(count == 0)total++;
        }
        return total;
    }
}
