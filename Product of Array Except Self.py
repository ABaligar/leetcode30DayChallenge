#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/
#My initial solution - 
'''Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        product = 1
        for i in nums:
            product *= i
            left_product.append(product) 
        product = 1
        for i in nums[::-1]:
            product *= i
            right_product.append(product)
        right_product = right_product[::-1]
        
        ret_list = []
        for i in range(len(nums)):
            left_result = right_result = 1
            if i > 0:
                left_result = left_product[i-1]
            if i < len(nums) - 1:
                right_result = right_product[i+1]
            ret_list.append(left_result * right_result)
        return ret_list
        
        
