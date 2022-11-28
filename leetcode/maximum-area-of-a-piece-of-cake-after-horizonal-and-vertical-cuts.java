// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts

import java.util.Arrays;

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        int maxH = Math.max(horizontalCuts[0], h-horizontalCuts[horizontalCuts.length-1]);
        int maxW = Math.max(verticalCuts[0], w-verticalCuts[verticalCuts.length-1]);
        for(int i = 1; i<horizontalCuts.length; i++)
            maxH = Math.max(maxH, horizontalCuts[i]-horizontalCuts[i-1]);
        for(int i = 1; i<verticalCuts.length; i++)
            maxW = Math.max(maxW, verticalCuts[i]-verticalCuts[i-1]);
        return (int)(((long)maxH * maxW)%1000000007);
    }
}