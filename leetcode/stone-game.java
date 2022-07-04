// https://leetcode.com/problems/stone-game/

import java.util.Arrays;

class Solution {
	// Optimal Solution Due To Question Premise
    public boolean stoneGameTrick(int[] piles) {        
        return true;
    }

	public boolean stoneGameProperDFSCacheing(int[] piles) {        
		// dp[i][j] is the max value Alice can achieve in subarray piles[i] through piles[j]
		int[][] dp = new int[piles.length][piles.length];
		return dfs(dp, piles, 0, piles.length-1) > (Arrays.stream(piles).sum()/2);        
	}
	
	// Find max value Alice can take in this subarray
	private int dfs(int[][] dp, int[] piles, int left, int right){
		// Base case
		if(left > right) return 0;
		
		// If value has been calculated
		if(dp[left][right] != 0) {
			return dp[left][right];
		}
		
		// Check if Alice's turn (even number of elements remaining)
		if((right - left) % 2 != 0){
			dp[left][right] = Math.max(dfs(dp, piles, left+1, right) + piles[left], dfs(dp, piles, left, right-1) + piles[right]);
		}else{ //Bob's turn, carry Alice's values forward 1 turn
			dp[left][right] = Math.max(dfs(dp, piles, left+1, right), dfs(dp, piles, left, right-1));
		}
			
		return dp[left][right];
	}
}
