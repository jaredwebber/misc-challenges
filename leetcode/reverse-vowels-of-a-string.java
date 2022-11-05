// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int left = 0;
        int right = chars.length-1;

        while(left <= right){
            while(left < right && !((""+chars[left]).matches("[aeiouAEIOU]")))
                left++;
            while(right > left && !((""+chars[right]).matches("[aeiouAEIOU]")))
                right--;
            char temp = chars[left];
            chars[left++] = chars[right];
            chars[right--] = temp;
        }

        return new String(chars);
    }
}