//https://leetcode.com/problems/longest-substring-without-repeating-characters/

import java.util.HashMap;

class Solution {    
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        char[] str = s.toCharArray();
        int currLength = 0;
        int maxLength = 0;
        
        for(int i = 0; i<str.length; i++ ){
            if(map.get(str[i]) == null){
                map.put(str[i], i);
                currLength++;
            }else{
                int lastSeen = map.get(str[i]);
                if(i - lastSeen <= currLength) currLength = i - lastSeen;
                else currLength++;
                map.put(str[i], i);
            }
            maxLength = Math.max(currLength, maxLength);
        }
        
        return maxLength;
    }
}