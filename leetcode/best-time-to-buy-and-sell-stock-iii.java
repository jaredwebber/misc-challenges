// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution {
    public int maxProfit(int[] prices) {
        int buyOne = -prices[0];
        int sellOne = 0;
        int buyTwo = -prices[0];
        int sellTwo = 0;
        
        for(int i = 1; i<prices.length; i++){
            buyOne = Math.max(buyOne, -prices[i]);
            sellOne = Math.max(sellOne, prices[i]+buyOne);
            buyTwo = Math.max(buyTwo, sellOne-prices[i]);
            sellTwo = Math.max(sellTwo, prices[i]+buyTwo);
        }
        
        return sellTwo;
    }
}
