# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        diff_with_previous_day = []
        for i in range(1, len(prices)):
            diff_with_previous_day.append(prices[i] - prices[i-1])
        ret_val = 0
        for number in diff_with_previous_day:
            if number > 0:
                ret_val += number
        return ret_val
        
