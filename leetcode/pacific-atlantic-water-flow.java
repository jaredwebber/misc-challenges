import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
	public List<List<Integer>> pacificAtlantic(int[][] heights) {
	   List<List<Integer>> coords = new ArrayList<List<Integer>>();
	   boolean[][] visited = new boolean[heights.length][heights[0].length];
	   boolean[] flow = new boolean[2];
		
	   for(int i = 0; i < heights.length; i++) {
		   for(int j = 0; j < heights[0].length; j++) {
			   flow[0] = false;
			   flow[1] = false;
			   dfs(heights,i, j, flow, visited);
			   if(flow[0] && flow[1]) coords.add(Arrays.asList(i, j));
		   }
	   }
	   return coords;
   }
   
   private void dfs(int[][] heights, int row, int col, boolean[] flow, boolean[][] visited) {
	   if((!flow[0] || !flow[1]) && (row < heights.length && col < heights[0].length && row >= 0 && col >=0 && !visited[row][col])){
	   
		   visited[row][col] = true;
		   
		   if(row == 0 || col == 0) flow[0] = true; //reached pacific ocean
		   if(row == heights.length-1 || col == heights[0].length-1) flow[1] = true; //reached atlantic ocean

		   if(row+1 < heights.length) {
			   if(heights[row][col] >= heights[row+1][col])
				   dfs(heights, row+1, col, flow, visited);
		   }
		   if(col+1 < heights[0].length) {
			   if(heights[row][col+1] <= heights[row][col])
				   dfs(heights, row, col+1, flow, visited);
		   }
		   if(row-1 >= 0) {
			   if(heights[row-1][col] <= heights[row][col])
				   dfs(heights, row-1, col, flow, visited);
		   }
		   if(col-1 >= 0) {
			   if(heights[row][col-1] <= heights[row][col])
				   dfs(heights, row, col-1, flow, visited);
		   }
		   
		   // Reset visited matrix
		   visited[row][col] = false;
	   }
   }
}

