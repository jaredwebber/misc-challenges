//https://leetcode.com/problems/counting-bits/

import java.util.ArrayList;

class Solution {
    ArrayList<Integer> memory = new ArrayList<Integer>();
    public int[] countBits(int n) {
        int[] output = new int[n+1];
        for(int i = 0; i<=n; i++){
            if(memory.size()>i){
                output[i] = memory.get(i);
            }else{
                int count = 0;
                String curr = Integer.toBinaryString(i);
                for(int j = 0; j<curr.length();j++){
                    if(curr.charAt(j) == '1'){
                        count++;
                    }
                }
                output[i] = count;
                memory.add(i, count);
            }
        }
        return output;
    }
}