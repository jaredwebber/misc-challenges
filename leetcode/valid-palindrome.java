// https://leetcode.com/problems/valid-palindrome/

class Solution {
    public boolean isPalindrome(String s) {
        char[] input = s.toCharArray();
        int left = 0;
        int right = input.length-1;
        
        while(left<right){
            while(!Character.isLetterOrDigit(input[left]) && left < right) left++;
            while(!Character.isLetterOrDigit(input[right]) && left < right) right--;
            if(!(""+input[left++]).equalsIgnoreCase(""+input[right--])) return false;
        }
        return true;
    }
}
