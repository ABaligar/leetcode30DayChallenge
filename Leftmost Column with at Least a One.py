#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [self.rows,self.cols] = binaryMatrix.dimensions()
        self.bm = binaryMatrix
        self.row_col_map = [-1]*self.rows
        for i in range(self.rows):
            self.binarySearchfirst1InBMRow(i)
        
        result = min(self.row_col_map)
        if result == 200:
            return -1
        return result
    
    def binarySearchfirst1InBMRow(self, row):
        low = 0
        high = self.cols - 1
        while(low <= high):
            mid = int(low + (high - low)/2)
            if self.bm.get(row, mid) == 1:
                high = mid - 1
            else:
                low = mid + 1
        result = 200
        if low >= 0 and low < self.cols and self.bm.get(row, low) == 1:   ## Dont forget to limit check here
            result = low
        elif high >= 0 and high < self.cols and self.bm.get(row, high) == 1:
            result = high
        self.row_col_map[row] = result
        
            
