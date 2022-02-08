//https://leetcode.com/problems/climbing-stairs/

//fibonacci sequence

//Version Three - Optimized for speed & (some) space
class Solution {
    public int climbStairs(int n) {
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
}


/* Version Two - Optimized for speed
class Solution {
    public int climbStairs(int n) {
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
}
*/

/* Version One - UnOptimized:
import java.util.ArrayList;

class Solution {
    ArrayList<Integer> memory = new ArrayList<Integer>();
    public int climbStairs(int n) {
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

*/
