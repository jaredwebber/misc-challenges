//https://leetcode.com/problems/coin-change/

import java.util.Arrays;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] sums = new int[amount+1];
        
        Arrays.fill(sums, amount+1);
        sums[0] = 0;
        
        for(int i = 1; i<=amount; i++){
            for(int j:coins){
                if(i-j >= 0) sums[i] = Math.min(sums[i-j]+1, sums[i]);
            }
        }
                
        return sums[amount] != amount+1 ? sums[amount] : -1;
    }
}
