#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        #calculate the net shift
        net_shift = 0
        for entry in shift:
            net_shift += ((-1 if entry[0] == 0 else 1) * entry[1])
            net_shift %= len(s)  ##### VERY VERY IMP STEP
        #ret_val = ''
        '''if net_shift < 0:
            ret_val = s[abs(net_shift):] + s[:abs(net_shift)]
        else:'''
        return s[-net_shift:] + s[:-net_shift]
        
        #return ret_val
        
