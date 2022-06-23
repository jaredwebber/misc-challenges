//https://leetcode.com/problems/climbing-stairs/

import java.util.ArrayList;

//fibonacci sequence
class Solution {
    //Version Four - Optimized for space
    public int climbStairs(int n) {
        int one = 1;
        int two = 2;
        for(int i = 3; i<=n; i++){
            if(i % 2 == 0) two += one;
            else one+=two;
        }   
        return n <= 3 ? n : Math.max(one, two);
    }

    //Version Three - Optimized for speed & (some) space
    public int climbStairsV3(int n) {
        int[] mem = new int[3];
        if(n == 0 || n == 1 || n == 2){
            return n;
        }else{
            mem[0] = 0;
            mem[1] = 1;
            mem[2] = 2;
            
            int index = 3;
            while(index<=n){
                mem[0] = mem[1];
                mem[1] = mem[2];
                mem[2] = mem[0] + mem[1];
                index++;
            }
        }
        return mem[2];
    }

    //Version 2 - Optimized for speed
    public int climbStairsV2(int n) {
        int[] mem = new int[n+1];
        if(n == 0 || n == 1 || n == 2){
            return n;
        }else{
            mem[0] = 0;
            mem[1] = 1;
            mem[2] = 2;
            
            int index = 3;
            while(index<=n){
                mem[index] = mem[index-1] + mem[index-2];
                index++;
            }
        }
        return mem[n];
    }

    //Version 1 - Unoptimized
    public int climbStairsV1(int n) {
        ArrayList<Integer> memory = new ArrayList<Integer>();
        if(n == 0 || n == 1 || n == 2){
            return n;
        }else{
            memory.add(0);
            memory.add(1);
            memory.add(2);
            
            int index = 3;
            while(index<=n){
                memory.add(index, memory.get(index-1)+memory.get(index-2));
                index++;
            }
        }
        return memory.get(n);
    }
}
