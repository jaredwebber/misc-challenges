//https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

//unoptimized

class Solution {
    public int[] minOperations(String boxes) {
        int[] ops = new int[boxes.length()];
        int[] box = new int[boxes.length()];

        for(int i = 0; i<box.length; i++){
            box[i] = Character.getNumericValue(boxes.charAt(i));
        }
        
        for(int i = 0; i<box.length; i++){
            for(int j = 0; j<box.length; j++){
                if(i!=j && box[j]==1) ops[i]+=Math.abs(i-j);
            }
        }
        return ops;
    }
}