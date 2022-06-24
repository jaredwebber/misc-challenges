//https://leetcode.com/problems/number-of-islands/

class Solution {
    public int numIslands(char[][] grid) {
		// Can be optimized for constant space by manipulating grid directly
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int counter = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j<grid[0].length; j++){
                if(grid[i][j] == '1' && !visited[i][j]) {
                    recurse(i, j, visited, grid);
                    counter++;
                }
            }
        }	

        return counter;
    }	

    private void recurse(int row, int col, boolean[][] visited, char[][] grid) {
        if(	row >= 0 && row < grid.length && col >= 0 && col < grid[0].length && !visited[row][col]){
            visited[row][col] = true;
            if(grid[row][col] == '1'){
                recurse(row + 1, col, visited, grid);
                recurse(row - 1, col, visited, grid);
                recurse(row, col + 1, visited, grid);
                recurse(row, col - 1, visited, grid);
            }
        }
    }
}
