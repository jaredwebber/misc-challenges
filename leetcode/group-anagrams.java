//https://leetcode.com/problems/group-anagrams/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> anagramGroups = new ArrayList<List<String>>();
        List<String> group = null;
        boolean placed = false;
        
        for(String i:strs){
            placed = false;
            for(List<String> s:anagramGroups){
                if(isAnagram(i, s.get(0))){
                    s.add(i);
                    placed = true;
                    break;
                }
            }
            if(!placed){
                group = new ArrayList<String>();
                group.add(i);
                anagramGroups.add(group);
            }
        }
        
        return anagramGroups;
    }
    
    private boolean isAnagram(String one, String two){
        if(one.length() != two.length()) return false;
        char[] first = one.toCharArray();
        char[] second = two.toCharArray();
        Arrays.sort(first);
        Arrays.sort(second);
        return Arrays.equals(first, second);
    }
}