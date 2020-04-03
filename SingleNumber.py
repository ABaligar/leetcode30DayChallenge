# Single Number
# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return_number = 0
        for number in nums:
            return_number ^= number
        return return_number
        
