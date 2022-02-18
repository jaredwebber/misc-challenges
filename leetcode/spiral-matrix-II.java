//https://leetcode.com/problems/spiral-matrix-ii/

class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int row = 0;
        int col = 0;
        int curr = 0;
        int goal = n*n;
        while(row < n && col< n){
            //right
            for(int i = col; i<n-col; i++){
                matrix[row][i] = ++curr;
            }
            row++;
            if(curr == goal) break;
            
            //down
            for(int i = row; i<=n-row; i++){
                matrix[i][n-col-1] = ++curr;
            }
            col++;
            if(curr == goal) break;
            
            //left
            for(int i = n-col-1; i>=col-1; i--){
                matrix[n-row][i] = ++curr;
            }
            
            //up
            for(int i = n - row-1; i>=row; i--){
                matrix[i][col-1] = ++curr;
            }
        }
        
        return matrix;
    }
}
