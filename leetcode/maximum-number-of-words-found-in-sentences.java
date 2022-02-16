//https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for(String i:sentences){
            max = Math.max(max, i.split(" ").length);
        }
        return max;
    }
}
