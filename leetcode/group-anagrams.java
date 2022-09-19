//https://leetcode.com/problems/group-anagrams/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap<String, List<String>>();
        
        for(int i = 0; i<strs.length; i++){
            char[] hashArr = strs[i].toCharArray();
            Arrays.sort(hashArr);
            String hash = new String(hashArr);
            
            List<String> group = groups.get(hash);
            if(group == null){
                group = new ArrayList<String>();
            }
            
            group.add(strs[i]);
            groups.put(hash, group);
        }
        
        List<List<String>> output = new ArrayList<List<String>>();
        for(String i: groups.keySet()){
            
            output.add(groups.get(i));
        }
        
        return output;
    }
}