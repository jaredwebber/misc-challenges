//https://leetcode.com/problems/spiral-matrix-iii/

class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int[][] coords = new int[rows*cols][2];
        int index = 0;
        int rad = 0;
        
        while(index < rows*cols){
            // travel right
            rad++;
            for(int i = 0; i<rad; i++){
                if(rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols){
                    coords[index][0] = rStart;
                    coords[index++][1] = cStart;
                }
                cStart++;
            }
            
            // travel down
            for(int i = 0; i<rad; i++){
                if(rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols){
                    coords[index][0] = rStart;
                    coords[index++][1] = cStart;
                }
                rStart++;
            }
            
            // travel left
            rad++;
            for(int i = 0; i<rad; i++){
                if(rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols){
                    coords[index][0] = rStart;
                    coords[index++][1] = cStart;
                }
                cStart--;
            }
            
            // travel up
            for(int i = 0; i<rad; i++){
                if(rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols){
                    coords[index][0] = rStart;
                    coords[index++][1] = cStart;
                }
                rStart--;
            }
        }
        
        return coords;
    }
}