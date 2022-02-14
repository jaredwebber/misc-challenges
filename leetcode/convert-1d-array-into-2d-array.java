//https://leetcode.com/problems/convert-1d-array-into-2d-array/
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if(original.length != m*n) return new int[0][0];
        
        int[][] twod = new int[m][n];
        for(int i = 0; i<original.length; i++){
            twod[i/n][i%n] = original[i];
        }
        return twod;
    }
}
