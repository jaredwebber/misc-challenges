//https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] answers = new int[queries.length];
        for(int i = 0; i<queries.length; i++){
            for(int j = 0; j<points.length; j++){
                if(Math.sqrt(Math.pow(Math.abs(points[j][0]-queries[i][0]),2)+Math.pow(Math.abs(points[j][1]-queries[i][1]),2)) <= queries[i][2] )
                    answers[i]++;
            }
        }
        return answers;
    }
}


