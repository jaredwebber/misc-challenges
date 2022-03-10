//https://leetcode.com/problems/string-to-integer-atoi/

//Somewhat inefficient, rules unclear in question

class Solution {
    public int myAtoi(String s) {
        boolean hasSign = false;
        char[] str = s.trim().toCharArray();
        String strVal = "";
        
        for(char i:str){
            if((i == '+' || i == '-') && hasSign) break;
            if(i == '+' ){
                hasSign = true;
                continue;
            }
            if(i == '-'){
                hasSign = true;
                strVal += "-";
            }else{
                try{
                    int digit = Integer.parseInt(String.valueOf(i));
                    strVal+=digit;
                    if(Long.parseLong(strVal) > Integer.MAX_VALUE) return Integer.MAX_VALUE;
                    if(Long.parseLong(strVal) < Integer.MIN_VALUE) return Integer.MIN_VALUE;
                    hasSign = true;
                }catch(Exception e){
                    
                    break;
                }
            }
        }
                
        try{
            return Integer.parseInt(strVal);
        }catch(Exception e){
            return 0;
        }
        
    }
}
