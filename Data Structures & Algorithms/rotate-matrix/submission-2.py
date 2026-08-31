class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #the space cooelxity must be O(1)
        #we go theough whole n by n matrix 

        #rotate in place by 90 and we do an offset by 1 

        left, right = 0, len(matrix[0]) - 1 

        while left < right:
            top, bottom = left, right 

            for i in range(right - left):
                topLeft = matrix[top][left + i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft
            


            left += 1 
            right -= 1
        
        



        
     

      





        