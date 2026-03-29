class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l , r = 0, (rows * cols) - 1
        while l <= r:
            mid = l + int((r - l) / 2)
            row = mid // cols # How many full rows have we completed 
            col = mid % cols # How many steps are we into the current row
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False