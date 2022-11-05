// https://leetcode.com/problems/smallest-even-multiple/submissions/

class Solution {
    public int smallestEvenMultiple(int n) {
        return (n % 2 == 0) ? n : n*2;
    }
}
