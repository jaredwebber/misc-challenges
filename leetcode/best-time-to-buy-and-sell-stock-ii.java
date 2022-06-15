//https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution {
    public int maxProfit(int[] prices) {
        int sum = 0;
        for(int i = prices.length-2; i >= 0; i--){
            if(prices[i+1] > prices[i]) sum+=prices[i+1]-prices[i];
        } 
        return sum;
    }
}
