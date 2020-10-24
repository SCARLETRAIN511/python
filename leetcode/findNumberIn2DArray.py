#python3

class Solution:
    def findNumberIn2DArray(self,matrix,target:int) -> bool:
        #matrix is list[list]
        i,j = len(matrix) - 1,0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(s.findNumberIn2DArray(matrix,7))