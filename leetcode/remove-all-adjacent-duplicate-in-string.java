// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

// There exists a more efficient Stack approach 
class Solution {
    public String removeDuplicates(String s) {
        int curr = 0;
        while(curr < s.length()-1){
            if(s.charAt(curr) != s.charAt(curr+1)){
                curr++;
            }else{
                s = s.substring(0,curr) + s.substring(curr+2, s.length());
                if(curr > 0) curr--;
            }
        }
        return s;
    }
}
