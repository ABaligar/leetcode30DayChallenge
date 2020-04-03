# Maximum Subarray
# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3285/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #store_max_sum_till_now
        #Keep adding elements to current sum as long as it is +v. 
        # Update the max_sum if required at every step
        if not nums:
            return
        max_sum = current_sum = nums[0]
        for number in nums[1:]:
            if (current_sum < 0):
                current_sum = number
            else:
                current_sum += number
            #this was initially under the first if, but it will not work with negative numbers and min one number criteria if it is inside
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum
