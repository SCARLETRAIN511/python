#python3

class Solution:
    def rotate(self,matrix) -> None:
        #matrix is a list with list in it
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in range(n):
            matrix[i].reverse()
        
#complexity of O(n^2)
class Solution2:
    def rotate(self,matrix) -> None:
        n = len(matrix[0])
        for i in range(n//2 + n%2):
            for j in range(n//2):
                tmp = [0] * 4
                row,col = i,j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row,col = col, n-1-row
                for k in range(4):
                    matrix[row][col] = tmp[(k-1)%4]
                    row,col = col,n-1-ro