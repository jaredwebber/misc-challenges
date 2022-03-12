//https://leetcode.com/problems/generate-parentheses/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        return generate(new ArrayList<String>(), "(", 1, n);
    }
    
    private List<String> generate(List<String> list, String curr, int open, int size){
        if(open<=size && open >= 0 && curr.length() <= size*2){
            if(curr.length() == size*2 && open==0) list.add(curr);
            else{
                if(open>0) generate(list, curr+")", open-1, size);
                if(open<size) generate(list, curr+"(", open+1, size);
            }
        }
        return list;
    }
}