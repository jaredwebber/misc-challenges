//https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    public int closedIsland(int[][] grid) {
        int count = 0;
        
        // Recursively set any islands touching the outer edge
        // of the grid to 1
        
        // Remove Top + Bottom Rows
        for(int i = 0; i<grid[0].length; i++){
            search(grid, 0,i);
            search(grid, grid.length-1,i);
        }
        
        // Remove Left + Right Columns
        for(int i = 1; i<grid.length-1; i++){
            search(grid, i,0);
            search(grid, i,grid[0].length-1);
        }
        
        // Run standard # of islands
        for(int i = 1; i<grid.length-1; i++){
            for(int j = 1; j<grid[0].length-1; j++){
                if(grid[i][j] == 0){
                    search(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private void search(int[][] grid, int row, int col){
        if(row >= 0 && row < grid.length && col >=0 && col < grid[0].length && grid[row][col] == 0){
            grid[row][col] = 1;
            search(grid, row+1, col);
            search(grid, row-1, col);
            search(grid, row, col+1);
            search(grid, row, col-1);
        }
    }
    
}