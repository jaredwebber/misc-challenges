// https://leetcode.com/problems/reshape-the-matrix/description/

class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(r*c != mat.length*mat[0].length) return mat;
        int[][] newMat = new int[r][c];
        int row = 0;
        int col = 0;
        for(int i = 0; i<mat.length; i++){
            for(int j = 0; j<mat[0].length; j++){
                newMat[row][col++] = mat[i][j];
                if(col > c-1){
                    row++;
                    col = 0;
                }
            }
        }
        return newMat;
    }
}
