#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #traverse from back
        #S = "ab#c", T = "ad#c
        #ab##", T = "c#d#
        #S = "a##c", T = "#a#c"
        #S = "a#c", T = "b"
        ##S a## T a
        # ab   asld###b#bjkf###
        
        s_index = len(S) - 1
        t_index = len(T) - 1
        
        while s_index > -1 or t_index > -1:
            print(s_index, t_index)
            if s_index > -1 and t_index > -1 and S[s_index] != '#' and T[t_index] != '#':
                if S[s_index] != T[t_index]:
                    return False
                else:
                    s_index -= 1
                    t_index -= 1
            else:
                print("s and t")
                print(s_index,1,t_index)
                if s_index > -1 and S[s_index] == '#':
                    #find_next_valid_index
                    count = 1
                    s_index -= 1
                    while count and s_index > -1:
                        if S[s_index] == '#':
                            count += 1
                        else:
                            count -= 1
                        s_index -= 1
                elif t_index == -1:
                    print("comin here??")
                    return False
                
                
                if t_index > -1 and T[t_index] == '#':
                    #find_next_valid_index
                    count = 1
                    t_index -= 1
                    while count and t_index > -1:
                        if T[t_index] == '#':
                            count += 1
                        else:
                            count -= 1
                        t_index -= 1
                elif t_index != -1 and s_index == -1:    ####OMG do it again 
                    return False
                
        print(s_index,0,t_index)       
        if s_index == t_index and s_index == -1:
            return True
        return False
            
            
            
        '''#brute-force
        S_stack = []
        T_stack = []
        for char in S:
            if char != '#':
                S_stack.append(char)
            elif len(S_stack):
                S_stack.pop()
        for char in T:
            if char != '#':
                T_stack.append(char)
            elif len(T_stack):
                T_stack.pop()
        if ''.join(S_stack) == ''.join(T_stack):
            return True
        return False'''
        
        '''"bxj##tw"
"bxj###tw"'''
        
        '''"y#fo##f"
"y#f#o##f"'''
            
