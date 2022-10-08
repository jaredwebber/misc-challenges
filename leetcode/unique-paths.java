//https://leetcode.com/problems/unique-paths/

class Solution {
    // More space efficient solution
    public int uniquePaths(int m, int n) {
        int[][] grid = new int[m][n];
        
        grid[0][0] = 1;
        
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(i > 0) grid[i][j] += grid[i-1][j];
                if(j > 0) grid[i][j] += grid[i][j-1];
            }
        }
        
        return grid[m-1][n-1];
    }

    // Approach without bounds checking
    public int uniquePathsNoBounds(int m, int n) {
        int[][] grid = new int[m+1][n+1];
        grid[m][n-1] = 1;
        
        for(int i = m-1; i>=0; i--){
            for(int j = n-1; j>=0; j--){
                grid[i][j] = grid[i+1][j] + grid[i][j+1];
            }
        }
        
        return grid[0][0];
    }
}