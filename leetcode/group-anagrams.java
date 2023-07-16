//https://leetcode.com/problems/group-anagrams/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        List<List<String>> groups = new ArrayList<List<String>>();

        for (String i : strs) {
            char[] str = i.toCharArray();
            Arrays.sort(str);
            String key = new String(str);
            Integer index = map.get(key);
            if (index != null) {
                groups.get(index).add(i);
            } else {
                map.put(key, groups.size());
                List<String> list = new ArrayList<String>();
                list.add(i);
                groups.add(list);
            }
        }

        return groups;
    }
}
