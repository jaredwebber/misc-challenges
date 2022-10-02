// https://leetcode.com/problems/search-a-2d-matrix/

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int lo = 0;
        int hi = matrix.length-1;
                
        // find row
        while(lo <= hi){
            int mid = (lo+hi)/2;   
            if(matrix[mid][0] == target || matrix[mid][matrix[0].length-1] == target) return true;
            else if(matrix[mid][0] < target && matrix[mid][matrix[0].length-1] < target) lo = mid+1;
            else hi = mid-1;
        }
        
        
        int row = lo;
        if(row > matrix.length-1) return false;
        
        lo = 0;
        hi = matrix[0].length-1;
                        
        // find col
        while(lo < hi){
            int mid = (lo+hi)/2;
            if(matrix[row][mid] == target) return true;
            else if(matrix[row][mid] > target) hi = mid-1;
            else lo = mid+1;            
        }
                
        return matrix[row][lo] == target;
    }
}
