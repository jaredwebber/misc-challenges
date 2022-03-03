//https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] maxRows = new int[grid.length];
        int[] maxCols = new int[grid.length];
        int count = 0;
        
        //find highest val in each row and col
        for(int i = 0; i<grid.length; i++){
            for(int j = 0; j<grid.length; j++){
                maxRows[i] = Math.max(maxRows[i], grid[i][j]);
                maxCols[i] = Math.max(maxCols[i], grid[j][i]);
            }
        }

        //sum difference of each position with the amout
        //it could be increased without surpassing
        //the max of it's row and its column
        for(int i = 0; i<grid.length; i++){
            for(int j = 0; j<grid.length; j++){
                count+= Math.min(maxRows[i], maxCols[j])-grid[i][j];
            }
        }
        
        return count;        
    }
}