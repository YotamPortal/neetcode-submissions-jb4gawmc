class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dup_row = set()
        dup_col = set()
        box_dup = set()
        n = len(board)
        # Assuming n = 9
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
        
                # Define your unique keys
                row_key = (i, val)
                col_key = (j, val)
                box_key = (i // 3, j // 3, val) # Including val in the box key
        
                # Check for duplicates
                if row_key in dup_row or col_key in dup_col or box_key in box_dup:
                    return False # We found a duplicate!
            
                # If not found, add them to your sets
                dup_row.add(row_key)
                dup_col.add(col_key)
                box_dup.add(box_key)
        return True