// https://leetcode.com/problems/maximum-units-on-a-truck/

import java.util.Arrays;

class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int max = 0;
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        
        for(int[] i: boxTypes){
            if(i[0] <= truckSize){
                truckSize-=i[0];
                max+=i[1]*i[0];
            }else{
                while(truckSize > 0){
                    truckSize--;
                    max+=i[1];
                }
            }
        }
        
        return max;
    }
}
