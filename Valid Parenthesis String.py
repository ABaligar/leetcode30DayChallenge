#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/
#My solution using a stack and too many conditions to take care of (need to submit 5 times and fix things before program got accepted)

class Solution:
    def checkValidString(self, s: str) -> bool:
        temp_stack = []
        for char in s:
            #for ( add 1 and ) -1
            if char == '(':
                temp_stack.append(char)
                #balance_factor += 1
            elif char == ')':
                if not len(temp_stack):
                    return False
                if temp_stack[-1] == '(':
                    temp_stack.pop()
                else:
                    star_count = temp_stack.pop()
                    if temp_stack:
                        temp_stack.pop() #remove (
                        if temp_stack and type(temp_stack[-1]) == int:
                            temp_stack[-1] += star_count
                        else:
                            temp_stack.append(star_count)
                    else:
                        star_count -= 1
                        if star_count:
                            temp_stack.append(star_count)
            elif char == '*':
                if temp_stack and type(temp_stack[-1]) == int:
                    temp_stack[-1] += 1
                else:
                    temp_stack.append(1)
            print(temp_stack)
            
        if not temp_stack:
            return True
        stars_available = 0
        while(temp_stack):
            entry = temp_stack.pop()
            if entry == '(':
                if not stars_available:
                    return False
                else:
                    stars_available -= 1
                    if temp_stack and type(temp_stack[-1]) == int:
                        stars_available += temp_stack.pop()
            else:
                stars_available += entry
        return True
                
#Errichto's solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        balance_factor = 0
        for char in s:
            if char in ['(', '*']:
                balance_factor += 1
            else:
                balance_factor -= 1
            
            if balance_factor < 0:
                return False
        
        balance_factor = 0
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char in [')', '*']:
                balance_factor += 1
            else:
                balance_factor -= 1
            
            if balance_factor < 0:
                return False
        return True
            

