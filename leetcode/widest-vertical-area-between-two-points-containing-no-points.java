// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

import java.util.Arrays;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        Arrays.sort(points, (one, two) -> one[0] - two[0]);
        int max = 0;
        for(int i = 1; i<points.length; i++){
            if(points[i][0] - points[i-1][0] > max) max = points[i][0] - points[i-1][0];
        }
        return max;
    }
}