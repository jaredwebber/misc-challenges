// https://leetcode.com/problems/search-suggestions-system/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> results = new ArrayList<List<String>>();
        Arrays.sort(products);
        
        for(int i = 0; i<searchWord.length(); i++){
            ArrayList<String> currSearch = new ArrayList<String>();
            for(int j = 0; j<products.length && currSearch.size() < 3; j++){
                if(products[j].length() >= i+1 && searchWord.substring(0, i+1).equals(products[j].substring(0, i+1)))
                    currSearch.add(products[j]);
            }
            results.add(currSearch);
        }
        
        return results;
    }
}
