//https://leetcode.com/problems/unique-paths-ii/

class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int n = obstacleGrid.length-1;
        int m = obstacleGrid[0].length-1;
        
        if(obstacleGrid[n][m] == 1 || obstacleGrid[0][0] == 1) return 0;
        
        obstacleGrid[n][m] = -1;
        for(int i = n; i>=0; i--){
            for(int j = m; j>=0; j--){
                if(obstacleGrid[i][j] != 1){
                    if(i+1 <= n && obstacleGrid[i+1][j] != 1){
                        obstacleGrid[i][j]= obstacleGrid[i][j] +obstacleGrid[i+1][j];
                    }
                    if(j+1 <= m && obstacleGrid[i][j+1] != 1){
                        obstacleGrid[i][j]= obstacleGrid[i][j] +obstacleGrid[i][j+1];
                    }
                }
            }
        }
    
        return Math.abs(obstacleGrid[0][0]);
    }
}
