#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3303/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid[0]):
            return 0
        cached_results = {}
        def compute_min_path(row, col):
            if (row, col) not in cached_results:
                if row >= len(grid) or col >= len(grid[0]):
                    return 1000000 #stands for infinity
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return grid[row][col]
                min_sub_path = min(compute_min_path(row+1, col), compute_min_path(row, col+1))
                result = min_sub_path + grid[row][col]
                cached_results[(row, col)] = result
            return cached_results[(row, col)]
        
        return compute_min_path(0, 0)
            
