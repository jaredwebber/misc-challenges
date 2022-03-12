//https://leetcode.com/problems/most-common-word/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        int maxCount = 0;
        String maxWord = null;
        String[] words = null;
        
        HashMap<String, Integer> counts = new HashMap<String, Integer>();
        Set<String> ban = new HashSet<String>();

        for(String i:banned) ban.add(i);
        words = paragraph.toLowerCase().split("\\W+");
        
        for(String i:words){
            String curr = i.trim();
            if(!curr.isEmpty() && !ban.contains(curr)){
                if(counts.get(curr) == null){
                    counts.put(curr, 1);
                    if(maxCount == 0){
                        maxWord = curr;
                        maxCount = 1;
                    }
                }else{
                    int newCount = counts.get(curr)+1;
                    counts.replace(curr, newCount);
                    if(newCount>maxCount){
                        maxCount = newCount;
                        maxWord = curr;
                    }
                }
            }
        }
        return maxWord;
    }
}