grid = [['.', '.', '.', '.', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['.', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', '.'],
           ['O', 'O', 'O', 'O', '.', '.'],
           ['.', 'O', 'O', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.']]


def get_first_line(mylist):
    line = ''
    row = len(grid)
    column = len(grid[0])
    for i in range(0, row):
        for j in range(0, 2):
            print("("+str(i)+","+str(j)+")")
            line += mylist[i][j]

    return line


print(get_first_line(grid))