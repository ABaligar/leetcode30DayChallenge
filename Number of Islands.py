#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3302/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def DFS(row, col, grid):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == '0':
                return
            else:
                grid[row][col] = '0'
                DFS(row-1, col, grid)
                DFS(row+1, col, grid)
                DFS(row, col+1, grid)
                DFS(row, col-1, grid)               
        
        island_count = 0
        if not grid or not len(grid[0]):
            return island_count
        
        #traverse iteratively till you find 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    DFS(i, j, grid)
                    island_count += 1
        return island_count
        
