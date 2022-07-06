// https://leetcode.com/problems/sort-characters-by-frequency/

import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    public String frequencySort(String s) {
        HashMap<Character, Integer> freq = new HashMap<Character, Integer>();
        PriorityQueue<int[]> charMap = new PriorityQueue<int[]>((c, f)->Integer.compare(f[1], c[1]));
        
        String out = "";
        char[] word = s.toCharArray();
        
        for(int i = 0; i<word.length; i++){
            if(freq.get(word[i]) == null){
                freq.put(word[i], 1);
            }else{
                freq.put(word[i], freq.get(word[i])+1);
            }
        }
        
        for(Character i : freq.keySet()){
            charMap.offer(new int[]{i, freq.get(i)});
        }
        
        while(!charMap.isEmpty()){
            int[] curr = charMap.poll();
            for(int i = 0; i < curr[1]; i++) out += (char)curr[0];
        }
         
        return out;
    }
}


