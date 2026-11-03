from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. Validate all Rows and Columns simultaneously
        for r in range(9):
            row_dict = defaultdict(int)
            col_dict = defaultdict(int)
            
            for c in range(9):
                element_row = board[r][c]
                element_col = board[c][r]
                
                # Check for row duplicates
                if element_row.isdigit():
                    row_dict[element_row] += 1
                    if row_dict[element_row] == 2:
                        return False
                
                # Check for column duplicates
                if element_col.isdigit():
                    col_dict[element_col] += 1
                    if col_dict[element_col] == 2:
                        return False

        # 2. Validate all nine 3x3 sub-boxes
        # box_r and box_c loop through top-left coordinates of each 3x3 box: (0,0), (0,3), (0,6), (3,0)...
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                box_dict = defaultdict(int)
                
                # Iterate through the 9 cells inside the current 3x3 box
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        element_box = board[r][c]
                        
                        if element_box.isdigit():
                            box_dict[element_box] += 1
                            if box_dict[element_box] == 2:
                                return False
                                
        # If no duplicates are found anywhere, the board is valid
        return True