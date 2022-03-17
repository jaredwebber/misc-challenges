//https://leetcode.com/problems/fibonacci-number/

//O(1) space
class Solution {
    public int fib(int n) {
        if(n == 0) return 0;
        if(n == 1 || n == 2) return 1;
        
        int one = 1;
        int two = 1;

        for(int i = 3; i<=n; i++){
            if(i % 2 == 0) two += one;
            else one += two;
        }
        return Math.max(one, two);
    }
}

/*
class Solution {
    public int fib(int n) {
        int[] cache = new int[n+1];
        for(int i = 0; i<=n; i++){
            if(i<2) cache[i] = i;
            else cache[i] = cache[i-1] + cache[i-2];
        }
        return cache[n];
    }
}
*/