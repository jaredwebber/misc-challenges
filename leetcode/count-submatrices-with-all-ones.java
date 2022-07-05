//https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    /*
        E.g.
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]

        0 1 1 1
        1 1 2 2
        0 1 2 3
        
        E.g.
        [0,0,0],
        [0,1,0],
        [0,1,0],
        [1,1,1],
        [1,1,0]

        0 0 0
        0 1 0
        0 1 0
        1 1 1
        1 2 0
        
        return sum of new matrix
        
    */
    public int countSquares(int[][] matrix) {
        int count = 0;
        
        for(int i = 0; i<matrix.length; i++){
            for(int j = 0; j<matrix[0].length; j++){
                if(i > 0 && j >0 && matrix[i][j] == 1) matrix[i][j] += Math.min(Math.min(matrix[i-1][j], matrix[i][j-1]), matrix[i-1][j-1]);
                count += matrix[i][j];
            }
        }
        
        return count;
    }
}
