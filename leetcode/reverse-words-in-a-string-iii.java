// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder word = new StringBuilder();
        
        for(int i = 0; i<words.length; i++){
            StringBuilder sb = new StringBuilder(words[i]);
            word.append(sb.reverse().toString());
            if(i != words.length-1) word.append(" ");
        }
        
        return word.toString();
    }
}
