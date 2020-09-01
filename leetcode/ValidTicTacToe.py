#Python3

class Solution:
    def validTicTacToe(self,board) -> bool:
        first,second = "XO"
        xCount = sum(row.count(first) for row in board)
        oCount = sum(row.count(second) for row in board)

        def win(board,player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            
            return (player == board[1][1] == board[0][0] == board[2][2] or player == board[1][1] == board[0][2] == board[2][0])
            
        if oCount not in {xCount - 1,xCount}:
            return False

        if win(board,first) and xCount - 1 != oCount:
            return False
        
        if win(board,second) and xCount != oCount:
            return False
        
        return True