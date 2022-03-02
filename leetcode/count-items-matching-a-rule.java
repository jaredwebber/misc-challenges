//https://leetcode.com/problems/count-items-matching-a-rule/

import java.util.List;

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0;
        int ruleIndex = -1;
        if(ruleKey.equals("type")) ruleIndex = 0;
        else if(ruleKey.equals("color")) ruleIndex = 1;
        else ruleIndex = 2;
        
        for(List<String> i:items){
            if(i.get(ruleIndex).equals(ruleValue)) count++;
        }
        return count;
    }
}
