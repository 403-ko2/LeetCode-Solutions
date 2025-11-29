"""
Line by line:
First variable is for simplicity. since the length of the matrix is the same as the length of each array we can say len(matrix)

top and bottom variables are our pointers. One that starts at the beginning of the matrix and one at the end of the matrix.

the while loop will stop when the pointers equal each other. essentially when the pointers are in the middle of the matrix. We want this behavior because for this first pass we want to flip the top value
of each column . Once we get to the middle we would have already done this change on all of the columns. 
ex)
    [ 1, 2, 3]       [10,11,12]
    [ 4, 5, 6]  -->  [ 7, 8, 9]
    [ 7, 8, 9]  -->  [ 4, 5, 6]
    [10,11,12]       [ 1, 2, 3]

this is essentially what the logic inside the loop is doing. We set a temp variable to hold the initial value of the top value. we then switch the top value with the bottom value of the same colomn
and make the bottom value equal to our temp variable. successfully performing our swap and we do that for each colomn! after the logic runs we increment our top pointer and decrement our bottom pointer.
by doing this we go to the next row and look at that colomns value.

The next loop we perform out transpose. What this essentially is, is swapping the "x and y values" so the transpose of matrix[x][y] would be matrix[y][x].
so here we use the same swap logic. We set a temp variable to hold the initial value. we then transpose that value and make the value we switched it with equal to our temp variable.

Since the problem asked us to do this in place we simply just return the matrix!
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge_length = len(matrix)

        top = 0
        bottom = edge_length - 1

        while top < bottom:
            for col in range(edge_length):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row, edge_length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        return matrix
