// https://leetcode.com/problems/max-area-of-island/

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        for(int i = 0; i<grid.length; i++){
            for(int j = 0; j<grid[0].length; j++){
                if(grid[i][j] == 1){
                    max = Math.max(max, islandSize(grid, i, j, 0));
                }
            }
        }
        return max;
    }
    
    private int islandSize(int[][] grid, int i, int j, int size){
        if(i >= 0 && j>= 0 && i < grid.length && j < grid[0].length && grid[i][j] == 1){
            grid[i][j] = 0;
            size = 1+ 
                islandSize(grid, i+1, j, size) +
                islandSize(grid, i-1, j, size) +
                islandSize(grid, i, j+1, size) + 
                islandSize(grid, i, j-1, size);
        }
                
        return size;
    }
}