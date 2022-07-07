// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution {
    public int maxScore(int[] cardPoints, int k) {
        // k right, k left, k-n right + n left, k-n left + n right
        // Sum all left
        // Then select 1 right while reducing the side of left window
        
        int total = 0;
        int max = 0;
        for(int i = 0; i<k; i++) total += cardPoints[i];
        
        if(cardPoints.length == k) return total;
        
        max = total;
        for(int i = 0; i<k; i++){
            total = total + cardPoints[cardPoints.length-1-i] - cardPoints[k-1-i];
            max = Math.max(max, total);
        }
        
        return max;
    }
}


