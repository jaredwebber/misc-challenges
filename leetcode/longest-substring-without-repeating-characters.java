//https://leetcode.com/problems/longest-substring-without-repeating-characters/

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max = 0;
        int currLen = 0;
        char[] input = s.toCharArray();
        
        for(int i = 0; i<input.length; i++){
            Integer lastSeen = map.get(input[i]);
            if(lastSeen != null && i-lastSeen <= currLen){
                max = Math.max(max, currLen);
                currLen = i-lastSeen;
            }else{
                currLen++;
            }
    
            map.put(input[i], i);
        }
        
        return Math.max(max, currLen);
    }
}