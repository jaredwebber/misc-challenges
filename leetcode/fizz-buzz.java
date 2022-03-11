////https://leetcode.com/problems/fizz-buzz/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> fizzbuzz = new ArrayList<String>();
        for(int i = 1; i<=n; i++){
            if(i % 15 == 0) fizzbuzz.add("FizzBuzz");
            else if(i % 3 == 0) fizzbuzz.add("Fizz");
            else if(i % 5 == 0) fizzbuzz.add("Buzz");
            else fizzbuzz.add(""+i);
        }
        return fizzbuzz;
    }
}

/*
class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> fizzbuzz = new ArrayList<String>();
        for(int i = 1; i<=n; i++){
            String val = "";
            if(i % 3 == 0) val+="Fizz";
            if(i % 5 == 0) val+="Buzz";
            if(val == "") val+=i;
            fizzbuzz.add(val);
        }
        return fizzbuzz;
    }
}
*/