// https://leetcode.com/problems/unique-number-of-occurrences/description/

import java.util.*;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashSet<Integer> seen = new HashSet<Integer>();

        Arrays.sort(arr);

        int curr = arr[0];
        int occ = 1;
        for(int i = 1; i<arr.length; i++){
            if(arr[i] != curr){
                if(!seen.add(occ)) return false;
                occ = 0;
            }
            occ++;
            curr = arr[i];
        }

        return seen.add(occ);
    }
}
