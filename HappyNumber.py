#https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def isHappy(self, n: int) -> bool:
        previous_result = -1
        cached_results = {}
        
        while(n!=1 and n!= previous_result):
            previous_result = n
            digits = self.find_digits(n)
            if frozenset(digits) in cached_results:
                return False
            cached_results[frozenset(digits)] = False
            n = self.find_sum(digits)
            
        if n == 1:
            return True
        return False
    
    def find_digits(self, n):
        digits = []
        while n:
            digit = n % 10
            digits.append(digit)
            n /= 10
            n = int(n)
        return digits
    
    def find_sum(self, digits: list) -> int:
        sum = 0
        for digit in digits:
            sum += digit**2
        return sum
