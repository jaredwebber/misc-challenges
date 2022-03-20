//https://leetcode.com/problems/longest-substring-without-repeating-characters/

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() <= 1) return s.length();
        
        //character and index last seen
        HashMap<Character, Integer> seen = new HashMap<Character, Integer>();
        int start = 0;
        int max = 0;
        
        for(int i = 0; i<s.length(); i++){
            char curr = s.charAt(i);
            if(seen.containsKey(curr)){
                start = Math.max(start, seen.get(curr)+1);
            }
            seen.put(curr, i);
            max = Math.max(i-start+1, max);
        }

        
        return max;
    }
}