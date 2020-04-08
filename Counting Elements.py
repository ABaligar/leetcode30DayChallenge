#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/

class Solution:
    def countElements(self, arr: List[int]) -> int:
        helper_map = {}
        for element in arr:
            if element in helper_map:
                helper_map[element] += 1
            else:
                helper_map[element] = 1
        ret_val = 0
        for number in helper_map.keys():
            if number+1 in helper_map:
                ret_val += helper_map[number]
                
        return ret_val
