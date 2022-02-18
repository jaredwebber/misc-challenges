//https://leetcode.com/problems/sorting-the-sentence/

class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        String[] sentence = new String[words.length];
        for(String i:words){
            int index = Integer.parseInt(String.valueOf(i.charAt(i.length()-1)))-1;
            sentence[index] = i.substring(0, i.length()-1);
        }
        
        s = "";
        for(String i:sentence){
            s+=i+" ";
        }
        return s.trim();
    }
}
