//https://leetcode.com/problems/unique-paths/

class Solution {
    public int uniquePaths(int m, int n) {
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