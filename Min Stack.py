# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min == None or x < self.min:  ##not !self.min an 0 is a valid entry
            self.min = x
        self.stack.append((x, self.min))
        #print("+", self.stack)

    def pop(self) -> None:
        tmp = self.stack.pop()
        self.min = self.getMin()  #Remember this
        if tmp:
            return tmp[0]
        #print("+", self.stack)

    def top(self) -> int:
        #print("top", self.stack)
        if not len(self.stack):
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not len(self.stack):
            return None
        #print("min", self.stack)
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
