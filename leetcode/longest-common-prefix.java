//https://leetcode.com/problems/longest-common-prefix/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = "";
        Boolean processing = true;
        int index = 0;
        
        while(processing){
            for(String i:strs){
                if(i.length()-1<index) return prefix.substring(0,index);
                if(prefix.length()-1<index) prefix+=i.charAt(index);
                if(i.charAt(index) != prefix.charAt(index)) return prefix.substring(0,index);
            }
            index++;
        }
        return "";
    }
}
