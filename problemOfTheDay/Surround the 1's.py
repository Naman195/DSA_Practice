# matrix = [[1, 0, 0], 
#           [1, 1, 0], 
#           [0, 1, 0]]
# matrix = [[1]]
matrix = [
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
]


def isEvenZeroSurrounding(matrix, row, col):
    Zero_Count = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    
    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        
        if new_row >= 0 and new_row < len(matrix) and new_col >= 0 and new_col < len(matrix[0]) and matrix[new_row][new_col] == 0:
            Zero_Count += 1
    
    return Zero_Count % 2 == 0


def SurroundByOnes(matrix):
    
  
	
    count = 0
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                if isEvenZeroSurrounding(matrix, row, col):
                    count += 1
    
    return count
print(SurroundByOnes(matrix))
            
    