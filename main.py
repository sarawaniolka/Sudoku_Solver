# importing the library
import numpy as np

# creating the grid
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,1,0]]


def check(r,c,nb):
    global grid
    # check if the number is in the row
    for i in range(0,9):
        if grid[r][i] == nb:
            return False
    # check if the number is in the column
    for i in range(0,9):
        if grid[i][c] == nb:
            return False
    # cheick if the number is in the square
    # creating the 3 sections
    x0 = (c//3)*3
    y0 = (r//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == nb:
                return False
    return True

def solve():
    global grid
    for r in range(0,9):
        for c in range(0,9):
            if grid[r][c] == 0:
                for nb in range(0,10):
                    if check(r,c,nb):
                        grid[r][c] = nb
                        solve()
                        grid[r][c] = 0
                return
    print(np.matrix(grid))
    input('More possible solutions')
    
solve()