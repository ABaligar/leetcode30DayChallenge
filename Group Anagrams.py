# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            string_hash_value = 0
            for char in string:
                string_hash_value += hash(char)
            if string_hash_value in hash_map:
                hash_map[string_hash_value].append(string)
            else:
                hash_map[string_hash_value] = [string]
        return hash_map.values()
