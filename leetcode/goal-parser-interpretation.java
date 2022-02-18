//https://leetcode.com/problems/goal-parser-interpretation/

class Solution {
    public String interpret(String command) {
        String goal = "";
        int index = 0;
        while(index<command.length()){
            if(command.charAt(index) == 'G'){
                goal+='G';
                index++;
            }else if(command.charAt(index) == '(' && command.charAt(index+1) == ')'){
                goal+='o';
                index+=2;
            }else{
                goal+="al";
                index+=4;
            }   
        }
        return goal;
    }
}
