//https://leetcode.com/problems/plus-one/

class Solution {
    public int[] plusOne(int[] digits) {
       if(digits[digits.length-1] < 9){
           digits[digits.length-1]++;
       }else{
           int index = digits.length-1;
           digits[digits.length-1]++;
           while(index >= 0 && digits[index] > 9){
               digits[index] = 0;
               if(index-1 >= 0) digits[index-1]++;
               else index = -8; //signal carry required (with -- nextline)
               index--;
           }
           if(index == -9 || digits[0] > 9){
               int[] increment = new int[digits.length+1];
               increment[0]++;
               return increment;
           }
       }
        return digits;
    }
}
