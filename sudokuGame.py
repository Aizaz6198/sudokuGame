# import random
# import math

# class Sudoku:
#     def __init__(self, N, K):
#         self.N = N
#         self.K = K

#         # Compute square root of N
#         SRNd = math.sqrt(N)
#         self.SRN = int(SRNd)
#         self.mat = [[0 for _ in range(N)] for _ in range(N)]
    
#     def fillValues(self):
#         # Fill the diagonal of SRN x SRN matrices
#         self.fillDiagonal()

#         # Fill remaining blocks
#         self.fillRemaining(0, self.SRN)

#         # Remove Randomly K digits to make game
#         self.removeKDigits()
    
#     def fillDiagonal(self):
#         for i in range(0, self.N, self.SRN):
#             self.fillBox(i, i)
    
#     def unUsedInBox(self, rowStart, colStart, num):
#         for i in range(self.SRN):
#             for j in range(self.SRN):
#                 if self.mat[rowStart + i][colStart + j] == num:
#                     return False
#         return True
    
#     def fillBox(self, row, col):
#         num = 0
#         for i in range(self.SRN):
#             for j in range(self.SRN):
#                 while True:
#                     num = self.randomGenerator(self.N)
#                     if self.unUsedInBox(row, col, num):
#                         break
#                 self.mat[row + i][col + j] = num
    
#     def randomGenerator(self, num):
#         return math.floor(random.random() * num + 1)
    
#     def checkIfSafe(self, i, j, num):
#         return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
    
#     def unUsedInRow(self, i, num):
#         for j in range(self.N):
#             if self.mat[i][j] == num:
#                 return False
#         return True
    
#     def unUsedInCol(self, j, num):
#         for i in range(self.N):
#             if self.mat[i][j] == num:
#                 return False
#         return True
    
   
#     def fillRemaining(self, i, j):
#         # Check if we have reached the end of the matrix
#         if i == self.N - 1 and j == self.N:
#             return True
    
#         # Move to the next row if we have reached the end of the current row
#         if j == self.N:
#             i += 1
#             j = 0
    
#         # Skip cells that are already filled
#         if self.mat[i][j] != 0:
#             return self.fillRemaining(i, j + 1)
    
#         # Try filling the current cell with a valid value
#         for num in range(1, self.N + 1):
#             if self.checkIfSafe(i, j, num):
#                 self.mat[i][j] = num
#                 if self.fillRemaining(i, j + 1):
#                     return True
#                 self.mat[i][j] = 0
        
#         # No valid value was found, so backtrack
#         return False

#     def removeKDigits(self):
#         count = self.K

#         while (count != 0):
#             i = self.randomGenerator(self.N) - 1
#             j = self.randomGenerator(self.N) - 1
#             if (self.mat[i][j] != 0):
#                 count -= 1
#                 self.mat[i][j] = 0
    
#         return

#     def printSudoku(self):
#         for i in range(self.N):
#             for j in range(self.N):
#                 print(self.mat[i][j], end=" ")
#             print()

# # Driver code
# if __name__ == "__main__":
#     N = 9
#     K = 40
#     sudoku = Sudoku(N, K)
#     sudoku.fillValues()
#     sudoku.printSudoku()


# updated code

import random
import math

class Sudoku:
    def __init__(self, N, K):
        # Validate inputs
        if N <= 0 or K < 0 or K > N * N:
            raise ValueError("Invalid Sudoku configuration.")
        
        self.N = N
        self.K = K

        # Compute square root of N
        self.SRN = int(math.sqrt(N))
        if self.SRN * self.SRN != N:
            raise ValueError("N must be a perfect square.")

        self.mat = [[0 for _ in range(N)] for _ in range(N)]

    def fill_values(self):
        # Fill the diagonal of SRN x SRN matrices
        self._fill_diagonal()

        # Fill remaining blocks
        self._fill_remaining(0, self.SRN)

        # Remove Randomly K digits to make game
        self._remove_k_digits()

    def _fill_diagonal(self):
        for i in range(0, self.N, self.SRN):
            self._fill_box(i, i)
    
    def _is_unused_in_box(self, row_start, col_start, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[row_start + i][col_start + j] == num:
                    return False
        return True

    def _fill_box(self, row, col):
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = random.randint(1, self.N)
                    if self._is_unused_in_box(row, col, num):
                        self.mat[row + i][col + j] = num
                        break
    
    def _is_safe(self, i, j, num):
        return (self._is_unused_in_row(i, num) and
                self._is_unused_in_col(j, num) and
                self._is_unused_in_box(i - i % self.SRN, j - j % self.SRN, num))
    
    def _is_unused_in_row(self, i, num):
        return num not in self.mat[i]
    
    def _is_unused_in_col(self, j, num):
        return all(self.mat[i][j] != num for i in range(self.N))

    def _fill_remaining(self, i, j):
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True
    
        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0
    
        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self._fill_remaining(i, j + 1)
    
        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self._is_safe(i, j, num):
                self.mat[i][j] = num
                if self._fill_remaining(i, j + 1):
                    return True
                self.mat[i][j] = 0
        
        # No valid value was found, so backtrack
        return False

    def _remove_k_digits(self):
        count = self.K
        while count != 0:
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if self.mat[i][j] != 0:
                self.mat[i][j] = 0
                count -= 1
    
    def print_sudoku(self):
        for row in self.mat:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

# Driver code
if __name__ == "__main__":
    N = 9
    K = 40
    sudoku = Sudoku(N, K)
    sudoku.fill_values()
    sudoku.print_sudoku()
