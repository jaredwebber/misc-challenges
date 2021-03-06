//https://leetcode.com/problems/minimum-path-sum/

class Solution {
    public int minPathSum(int[][] grid) {
        
        // First Row
        for(int i = 1; i<grid[0].length; i++){
            grid[0][i] += grid[0][i-1];
        }
        
        // First Column
        for(int i = 1; i<grid.length; i++){
            grid[i][0] += grid[i-1][0];
        }
        
        // Interior Grid
        for(int i = 1; i<grid.length; i++){
            for(int j = 1; j<grid[0].length; j++){
                grid[i][j] += grid[i-1][j] < grid[i][j-1] ? grid[i-1][j] : grid[i][j-1];
            }
        }
            
        return grid[grid.length-1][grid[0].length-1];
    }
}
