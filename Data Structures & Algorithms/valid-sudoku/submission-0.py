class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if( val == "."):
                    continue
                rowId = f"{val} in row {i}"
                colId = f"{val} in Col {j}"
                grp = f"{val} in block {i // 3} - {j // 3}"
                if( rowId in seen or colId in seen or grp in seen):
                    return False
                else:
                    seen.add(rowId)
                    seen.add(colId)
                    seen.add(grp)
        return True