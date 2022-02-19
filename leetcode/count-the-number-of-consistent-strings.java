//https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        boolean consistent = true;
        for(String i: words){
            consistent = true;
            for(int j = 0; j<i.length(); j++){
                if(!allowed.contains(String.valueOf(i.charAt(j)))) consistent = false;
            }
            if(consistent) count++;
        }
        
        return count;
    }
}
