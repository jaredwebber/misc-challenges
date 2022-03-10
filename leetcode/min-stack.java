//https://leetcode.com/problems/min-stack/

import java.util.ArrayList;

class MinStack {

    /**
     * Your MinStack object will be instantiated and called as such:
     * MinStack obj = new MinStack();
     * obj.push(val);
     * obj.pop();
     * int param_3 = obj.top();
     * int param_4 = obj.getMin();
     */

    ArrayList<Integer> stack;
    int min;
    
    public MinStack() {
        stack = new ArrayList<Integer>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        min = Math.min(min, val);
        stack.add(val);
    }
    
    public void pop() {
        if(min == stack.remove(stack.size()-1)){
            min = Integer.MAX_VALUE;
            for(int i:stack){
                min = Math.min(min, i);
            }
        }
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return min;
    }
}