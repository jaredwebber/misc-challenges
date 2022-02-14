//https://leetcode.com/problems/spiral-matrix/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> spiral = new ArrayList<Integer>();
        int rowsVisited = 0;
        int colsVisited = 0;
                
        while(rowsVisited < matrix.length && colsVisited < matrix[0].length){               
            //right
            for(int i = colsVisited; i<matrix[0].length-colsVisited; i++){
                spiral.add(matrix[rowsVisited][i]);
            }
            rowsVisited++;
            if(matrix.length*matrix[0].length == spiral.size()) break;
            //down
            for(int i = rowsVisited; i<matrix.length-(rowsVisited-1); i++){
                spiral.add(matrix[i][matrix[0].length - 1 - colsVisited]);
            }
            colsVisited++;
            if(matrix.length*matrix[0].length == spiral.size()) break;
            //left
            for(int i = matrix[0].length-colsVisited-1; i>=colsVisited-1; i--){
                spiral.add(matrix[matrix.length-rowsVisited][i]);
            }
            if(matrix.length*matrix[0].length == spiral.size()) break;
            //up
            for(int i = matrix.length-rowsVisited-1; i>=rowsVisited; i--){
                spiral.add(matrix[i][colsVisited-1]);
            }
            if(matrix.length*matrix[0].length == spiral.size()) break;
        }
        
        return spiral;
    }
}