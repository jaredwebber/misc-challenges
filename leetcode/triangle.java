//https://leetcode.com/problems/triangle/

import java.util.List;

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] sum = new int[triangle.size()][triangle.get(triangle.size()-1).size()];
        
        for(int i = 0; i<triangle.size(); i++) sum[sum.length-1][i] = triangle.get(triangle.size()-1).get(i);
        
        for(int i = sum.length-1; i >= 0; i--){
            for(int j = 1; j<=i; j++){
                sum[i-1][j-1] = triangle.get(i-1).get(j-1) + Math.min(sum[i][j-1], sum[i][j]);
            }
        }
        
        return sum[0][0];
    }
}
