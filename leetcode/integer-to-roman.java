//https://leetcode.com/problems/integer-to-roman/

class Solution {
    final int THOUSANDS = 3;
    final int HUNDREDS = 2;
    final int TENS = 1;
    final int ONES = 0;

    public String intToRoman(int num) {
        String numString = ""+num;
        int[] digits = new int[numString.length()];
        String roman = "";
        
        for(int i = 0; i<numString.length(); i++){
            digits[i] = Integer.parseInt(String.valueOf(numString.charAt(i)));
        }
        
        for(int i = 0; i<digits.length; i++){
            while(digits[i]>0){
                int index = digits.length-1 - i;
                if(index == THOUSANDS){
                    roman+="M";
                    digits[i]--;
                }else if(index == HUNDREDS && digits[i]==9){
                    roman+="CM";
                    digits[i]-=9;
                }else if(index == HUNDREDS && digits[i]==4){
                    roman+="CD";
                    digits[i]-=4;
                }else if(index == HUNDREDS && digits[i]-5>=0){
                    roman+="D";
                    digits[i]-=5;
                }else if(index == HUNDREDS){
                    roman+="C";
                    digits[i]-=1;
                }else if(index == TENS && digits[i]==9){
                    roman+="XC";
                    digits[i]-=9;
                }else if(index == TENS && digits[i]==4){
                    roman+="XL";
                    digits[i]-=4;
                }else if(index == TENS && digits[i]-5>=0){
                    roman+="L";
                    digits[i]-=5;
                }else if(index == TENS){
                    roman+="X";
                    digits[i]--;
                }else if(index == ONES && digits[i]==9){
                    roman+="IX";
                    digits[i]-=9;
                }else if(index == ONES && digits[i]==4){
                    roman+="IV";
                    digits[i]-=4;
                }else if(index == ONES && digits[i]-5>=0){
                    roman+="V";
                    digits[i]-=5;
                }else if(index == ONES){
                    roman+="I";
                    digits[i]--;
                } 
            }
        }
        
        return roman;
    }
}
