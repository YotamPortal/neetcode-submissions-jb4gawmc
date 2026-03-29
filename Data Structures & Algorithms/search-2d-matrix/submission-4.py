class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l , r = 0, (rows * cols) - 1
        while l <= r:
            mid = l + int((r - l) / 2)
            x , y =  mid // cols, mid % cols
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False