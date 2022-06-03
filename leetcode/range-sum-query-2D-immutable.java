//https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix {
    int[][] sumMatrix;
    
    public NumMatrix(int[][] matrix) { 
        sumMatrix = new int[matrix.length+1][matrix[0].length+1];
        for(int i = 0; i<matrix.length; i++){
            for(int j = 0; j<matrix[0].length; j++){
                sumMatrix[i+1][j+1] = matrix[i][j]+sumMatrix[i+1][j];
            }
        }        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for(int i = row1+1; i<=row2+1; i++){
            sum+=sumMatrix[i][col2+1] - sumMatrix[i][col1];
        }
        return sum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */