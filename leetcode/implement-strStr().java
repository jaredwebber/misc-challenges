//https://leetcode.com/problems/implement-strstr/

class Solution {
    public int strStr(String haystack, String needle) {
        char[] hay = haystack.toCharArray();
        char[] need = needle.toCharArray();
        
        if(need.length == 0) return 0;
        if(need.length > hay.length) return -1;

        for(int i = 0; i < hay.length; i++){
            if(hay[i] == need[0]){
                for(int j = 0; j<need.length && i+j < hay.length && hay[i+j] == need[j]; j++){
                    if(j == need.length-1) return i;
                }
            }
        }
        
        return -1;
    }
}