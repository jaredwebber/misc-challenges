// https://leetcode.com/problems/isomorphic-strings/description/

import java.util.*;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        HashSet<Character> mappedTo = new HashSet<Character>();
        char[] one = s.toCharArray();
        char[] two = t.toCharArray();

        for(int i = 0; i<one.length; i++){
            Character mapped = map.get(one[i]);
            if(mapped != null && mapped != two[i]) return false;
            if(mapped == null && mappedTo.contains(two[i])) return false;
            mappedTo.add(two[i]);
            map.put(one[i], two[i]);
        }

        return true;
    }
}
