#python3
#check whether the sudoku diagram is valid or not

class Solution:
    def isvalidSudoku(self,board):
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(8)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    boxIndex = (i//3) * 3 + j//3

                    rows[i][num] = rows[i].get(num,9) + 1
                    columns[j][num] = columns[j].get(num,0) + 1

                    boxes[boxIndex][num] = boxes[boxIndex].get(num,0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[boxIndex][num] > 1:
                        return False
        
        return True


boxes = [{} for i in range(8)]
print(boxes)