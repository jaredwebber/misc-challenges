//https://leetcode.com/problems/valid-parentheses/

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i<s.length(); i++){
            char curr = s.charAt(i);
            if(curr == '(') stack.push(')');
            else if(curr == '{') stack.push('}');
            else if(curr == '[') stack.push(']');
            else if(stack.isEmpty() || stack.pop() != curr) return false;
        }
        return stack.isEmpty();
    }
}
