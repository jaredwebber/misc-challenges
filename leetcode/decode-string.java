// https://leetcode.com/problems/decode-string/

import java.util.Stack;

class Solution {
    public String decodeString(String s) {        
        char[] input = s.toCharArray();
        int index = 0;
        Stack<String> stack = new Stack<String>();
        StringBuilder sb = new StringBuilder();
        String string = "";
        int mult = 1;
        
        while(index < input.length){           
            sb.setLength(0);
            mult = 1;
            string = "";
            
            // push until ]
            while(index < input.length && input[index] != ']') stack.push(""+input[index++]);
            index++;

            // build internal character string in reverse order popping until [
            while(!stack.isEmpty() && Character.isLetter(stack.peek().charAt(0))) sb.insert(0, stack.pop());
            // Pop [
            if(!stack.isEmpty() && stack.peek().equals("[")) stack.pop();
            string = sb.toString();
            
            sb.setLength(0);
            
            // build internal string multiplier in reverse order popping until not digit
            while(!stack.isEmpty() && stack.peek().length() == 1 && Character.isDigit(stack.peek().charAt(0))) sb.insert(0, stack.pop());
            if(sb.length() > 0) mult = Integer.parseInt(sb.toString());

            sb.setLength(0);
            
            // multiply string*multiplier, push to stack
            for(int i = 0; i<mult; i++){
                sb.insert(0, string);
            }
            
            if(sb.length() > 0) stack.push(sb.toString());
        }
        
        sb.setLength(0);
        
        // Build complete string using stack values
        while(!stack.isEmpty()){
            sb.insert(0, stack.pop());
        }
          
        return sb.toString();
    }
}
