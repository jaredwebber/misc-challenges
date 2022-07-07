//https://leetcode.com/problems/01-matrix/

class Solution {
    public int[][] updateMatrix(int[][] mat) {    
        
        // Using Integer.MAX_VALUE overflows into negatives
        // which leads to selection in Math.min()
        int maxVal = mat.length*mat[0].length;

        // Top left to bottom right
        for(int i = 0; i<mat.length; i++){
            for(int j = 0; j<mat[0].length; j++){
                if(mat[i][j] != 0){ 
                    int up = maxVal;
                    int left = maxVal;
                    
                    if(i > 0) up = mat[i-1][j];
                    if(j > 0) left = mat[i][j-1];
                    
                    mat[i][j] = Math.min(up, left) + 1;
                }
             }
        }
        
        // Bottom right to top left
        for(int i = mat.length-1; i>=0; i--){
            for(int j = mat[0].length-1; j >=0; j--){
                if(mat[i][j] != 0){ 
                    int down = maxVal;
                    int right = maxVal;
                    
                    if(i < mat.length-1) down = mat[i+1][j];
                    if(j < mat[0].length-1) right = mat[i][j+1];
                    
                    mat[i][j] = Math.min(Math.min(right, down) + 1, mat[i][j]);
                }
            }
        }
        
        return mat;
    }
}


