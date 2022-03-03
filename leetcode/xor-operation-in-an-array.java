//https://leetcode.com/problems/xor-operation-in-an-array/

class Solution {
    public int xorOperation(int n, int start) {
        int xor = start;
        for(int i = 0; i<n-1; i++){
            start+=2;
            xor = xor^start;
        }
        return xor;
    }
}
