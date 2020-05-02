#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #11110111100011001111110
        
        max_len = 0
        first_seen_index = {0:-1}  #Crucial initialization
        sum_till_i = 0
        for i in range(len(nums)):
            sum_till_i += (1 if nums[i] == 1 else -1)
            if sum_till_i in first_seen_index:
                new_sub_array_len = i - first_seen_index[sum_till_i]
                max_len = max(max_len, new_sub_array_len)
            else:
                first_seen_index[sum_till_i] = i  #Dont forget to record new values
        return max_len
