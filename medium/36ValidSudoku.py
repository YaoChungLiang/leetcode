class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                        if not self.is_valid(board, i,j, str(board[i][j])):
                            return False
        return True
                        
    def is_valid(self,board, row, col, num):      
        for i in range(9):
            if i!=row and board[i][col] == num:
                return False
        
            if i!=col and board[row][i] == num:
                return False
        
            rowIndex =  3*int(row/3) + int(i/3)
            colIndex =  3*int(col/3) + i%3
            if rowIndex!=row and colIndex!= col and board[rowIndex][colIndex] == num:
                return False
        
        return True
    
class SolutionForPramp:
    def isValidSudoku(self, board):
        return self.helper(board)
        
    def helper(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in range(1,10):
                        if self.is_valid(board, i,j, str(num)):
                            board[i][j] = str(num)
                            if self.helper(board):
                                return True
                        board[i][j] = "."
                    return False
        return True
                        
    def is_valid(self,board, row, col, num):      
        for i in range(9):
            if board[i][col] == num:
                return False
        
            if board[row][i] == num:
                return False
        
            rowIndex =  3*int(row/3)+ int(i/3)
            colIndex =  3*int(col/3) + i%3
            if board[rowIndex][colIndex] == num:
                return False
        
        return True
        
    def is_vad(self, board, ind_row, ind_col, possible_num):
        for i in range(9):
            if board[i][ind_col] == possible_num:
                return False
        for j in range(9):
            if board[ind_row][j] == possible_num:
                return False
        rowInd = int(ind_row/3*3)
        colInd = int(ind_col/3)*3
        for i in range(rowInd, rowInd+3):
            for j in range(colInd, colInd+3):
                print(rowInd)
                print(colInd)
                if board[i][j] == possible_num:
                    return False
        return True
    
if __name__ == "__main__":
    arr = [["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    print(sol.isValidSudoku(arr))