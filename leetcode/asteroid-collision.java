//https://leetcode.com/problems/asteroid-collision/

import java.util.Stack;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<Integer>();
        int index = 0;
        
        while(index < asteroids.length){
            if(stack.isEmpty()){
                stack.push(asteroids[index]);
                index++;
            }else{
                int topStack = stack.peek();
                if(topStack > 0 && asteroids[index] < 0){
                    if(topStack < -asteroids[index]){
                        stack.pop();
                    }else{
                        if(topStack == -asteroids[index]){
                            stack.pop();
                        }
                        index++;
                    }
                }else{
                    stack.push(asteroids[index]);
                    index++;
                }
            }
        }
        
        int arr[] = new int[stack.size()];
        index = stack.size()-1;
        while(!stack.isEmpty()){
            arr[index] = stack.pop();
            index--;
        }
        
        return arr;
    }
}



