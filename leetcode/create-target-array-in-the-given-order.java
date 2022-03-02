//https://leetcode.com/problems/create-target-array-in-the-given-order/

import java.util.ArrayList;

class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] target = new int[nums.length];
        ArrayList<Integer> construct = new ArrayList<Integer>();
        for(int i = 0; i<target.length; i++){
            construct.add(index[i], nums[i]);
        }
        for(int i = 0; i<target.length; i++){
            target[i] = construct.get(i);
        }
        return target;
    }
}
