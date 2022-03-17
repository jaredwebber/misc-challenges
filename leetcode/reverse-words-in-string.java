//https://leetcode.com/problems/reverse-words-in-a-string/

class Solution {
    public String reverseWords(String s) {
        String[] arr = s.trim().split(" ");
        
        s = "";
        for(int i = arr.length-1; i>=0; i--){
            if(!arr[i].trim().isEmpty()){
                s += arr[i].trim();
                if(i!=0) s+= " ";
            }
        }
        
        return s;
    }
}
