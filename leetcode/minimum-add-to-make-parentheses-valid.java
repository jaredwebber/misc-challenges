//https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
    public int minAddToMakeValid(String s) {
        int curr = 0;
        int add = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == '('){
                if(curr<0){
                    add+=Math.abs(curr);
                    curr = 1;
                }else curr++;
            }else curr--;
        }
        return add+Math.abs(curr);
    }
}
