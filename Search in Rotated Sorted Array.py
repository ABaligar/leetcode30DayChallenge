#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/
#BY_HEART the bloody program -- too many opportunities to inject bugs

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot ( min ele)
        if not nums or not len(nums):
            return -1
        low = 0
        high = len(nums) - 1
        
        while (low < high):   ########### not <=  if you put =, time limit exceeded
            mid = int(low + (high - low)/2)  ## correct way to find mid without overflow
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid     ############ this is now mid - 1, as mid element could be the min element
        
        start = low
        low = 0
        high = len(nums) -1
        
        #now we know the start element
        
        #now that we know the split, find out which part of that split has the element
        if target > nums[high]:  ############## again no = 
            high = start        ######## both are assigned start (no + or - 1)
        else:
            low = start     ######## both are assigned start (no + or - 1)
            
        #now write-up a normal binary search
        while (low <= high):   ######### this is normal bs with ''<=''
            mid = int(low + (high - low)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
            
                
