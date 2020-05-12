board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    print('\n\n')
    for i,row in enumerate(board):
        if i == 3 or i == 6:
            print('    ----------------------')
        line = '    '
        for j,num in enumerate(row):
            if j == 3 or j == 6: 
                line += '| '
            line += str(num) + ' '
        print(line)
    print('\n\n')
        

# Board -> First empty space
def get_empty(board):
    for i,row in enumerate(board):
        for j,num in enumerate(row):
            if num == 0:
                return i,j
    return None

# Board Number Coordinates -> See if the given number is valid in the given coordinate in the given baord
def is_valid(board, n, co):
    i,j = co

    # Check row
    if n in board[i]:
        # print("Number", n, "in row")
        return False

    # Check column
    for row in board:
        if row[j] == n:
            # print("Number", n, "in col")
            return False

    # Check box

    # Get position of i,j in the block
    i_pos = i%3
    j_pos = j%3

    for x in range(3):
        for y in range(3):
            i_check = i-i_pos+x
            j_check = j-j_pos+y
            if i != i_check and j != j_check:
                if board[i_check][j_check] == n: 
                    # print("Number", n, "in box")
                    return False

    # Else the number is fine
    return True

# Board -> Solves the board and returns it
def solver(baord):
    if not get_empty(baord): 
        return True

    co = get_empty(board)
    i,j = co
    for n in range(1,10):
        if is_valid(board, n, co):
            board[i][j] = n
            if solver(board): 
                return True
            board[i][j] = 0
    return False


if __name__ == "__main__":
    print_board(board)
    if solver(board):  
        print_board(board)
    else: print("No solution exists")
    


